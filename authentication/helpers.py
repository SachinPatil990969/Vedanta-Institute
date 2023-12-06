from django.http import JsonResponse

import os
import uuid
import random
import string
import jwt
import datetime

secret_key = "b379a78e02e5e3224865994e1a7446b1de58c917b03f58d219c271e0ef0fcc4e006d5ca3d65d986a066aad550c4e1800e33f283dc309ddf17f47175eae5edfc4"

def create_jwt_token(email):
    payload = {
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1), 
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def decode_jwt_token(token):
    payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    return payload

def require_access_token(view_func):
    def _wrapped_view(request, *args, **kwargs):
        token = request.session.get('token')  # Change this to how you store your token
        if token:
            try:
                payload = jwt.decode(token, secret_key, algorithms=['HS256'])
                # You can perform additional checks on the payload if needed
                return view_func(request, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                # Handle expired token
                return JsonResponse({'error': 'Token has expired'}, status=401)
            except jwt.DecodeError:
                # Handle invalid token
                return JsonResponse({'error': 'Invalid token'}, status=401)
        else:
            # Handle missing token (e.g., redirect to the login page)
            return JsonResponse({'error': 'Token required'}, status=401)
    return _wrapped_view