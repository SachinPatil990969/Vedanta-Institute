from django.urls import path
from .views import dashboard_view, student_view, teachers_view, course_view, books_view, updateStudent

urlpatterns = [
    path('', dashboard_view, name='dashboard_view'),
    path('student_view/', student_view, name='student_view'),
    path('teachers_view/', teachers_view, name='teachers_view'),
    path('course_view/', course_view, name='course_view'),
    path('books_view/', books_view, name='books_view'),
    path('updateStudent/<int:student_id>/',updateStudent, name = 'updateStudent')
]
