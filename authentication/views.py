from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .helpers import *
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            CHECK_MEMBER = adminModel.objects.get(email=email)
        except adminModel.DoesNotExist:
            messages.error(request, "Member does not exist")
            return render(request, 'login.html')
        else:
            if len(email) != 0 and len(password) != 0 and CHECK_MEMBER:
                if password == CHECK_MEMBER.password:
                    request.session['token'] = create_jwt_token(email)
                    return redirect('dashboard_view')
                else:
                    messages.error(request, "Incorrect Email or Password")
                    return render(request, 'login.html')
    return render(request, 'login.html')

@require_access_token
def logout(request):
    request.session.clear()
    messages.success(request, "You are logged out")
    return redirect('login_view')