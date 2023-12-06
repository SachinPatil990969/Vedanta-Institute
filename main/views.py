from django.shortcuts import render,redirect
from django.contrib import messages
from .models import studentModel,teachersModel,courseModel,booksModel

# Create your views here.
def dashboard_view(request):
     student_count = studentModel.objects.count()
     student_ = studentModel.objects.all()
     teachers_count = teachersModel.objects.count()
     teachers_ = teachersModel.objects.all()
     course_count = courseModel.objects.count()
     books_count = booksModel.objects.count()

     context = {
          'student_count': student_count,
          'teachers_count' : teachers_count,
          'course_count' : course_count,
          'books_count' : books_count,
          'student' : student_,
          'teachers' : teachers_

     }
     return render(request, 'dashborad.html' , context)


def student_view(request):
    if request.method == "POST":
        fname = request.POST['first-name']
        lname = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        course = request.POST['course']
        new_student = studentModel.objects.create(
            first_name = fname,
            last_name = lname,
            email= email,
            mobile=mobile,
            course_name_id=course
        )
        new_student.save()
        return redirect('student_view')
    student_ = studentModel.objects.all()
    courses_ = courseModel.objects.all()
    context = {
        'students' : student_,
        'courses':courses_
    }
    return render(request, 'student.html',context)

def updateStudent(request,student_id):
    if request.method == 'POST':
          fname = request.POST['first-name']
          lname = request.POST['last_name']
          email = request.POST['email']
          mobile = request.POST['mobile']
          course = request.POST['course']
          update_student = studentModel.objects.get(id=student_id)
          update_student.first_name = fname
          update_student.last_name = lname
          update_student.email = email
          update_student.mobile = mobile
          update_student.course_name_id = course
          update_student.save()
          return redirect('student_view')
    
    courses_ = courseModel.objects.all()
    update_student = studentModel.objects.get(id=student_id)
    context = {
        'first-name':update_student.first_name,
        'last_name': update_student.last_name,
        'email': update_student.email,
        'mobile': update_student.mobile,
        'course_name': update_student.course_name_id,
        'courses':courses_

    }
    return render (request,'update_student.html',context)

def teachers_view(request):
    if request.method == "POST":
        first_name = request.POST.get('full_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        course = request.POST.get('course')

        # Validate the data (add more validation as needed)
        if not first_name or not last_name or not email or not mobile or not course:
            messages.error(request, 'Please fill in all fields.')
            return redirect('teachers_view')

        # Create a new teachersModel instance
        new_teacher = teachersModel.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            course=course
        )

        # Save the new teacher instance
        new_teacher.save()

        messages.success(request, 'Teacher added successfully.')
        return redirect('teachers_view')

    # If the request method is not POST, render the teachers.html template with existing data
    teachers = teachersModel.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teachers.html', context)


def course_view(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course_faculty_name = request.POST.get('course_faculaty_name')
        course_duration = request.POST.get('course_duration')
        course_fees = request.POST.get('course_fees')

        # Validate the data (add more validation as needed)
        if not course_name or not course_faculty_name or not course_duration or not course_fees:
            messages.error(request, 'Please fill in all fields.')
            return redirect('course_view')

        # Create a new courseModel instance
        new_course = courseModel.objects.create(
            course_name=course_name,
            course_faculaty_name=course_faculty_name,
            course_duration=course_duration,
            course_fees=course_fees
        )

        # Save the new course instance
        new_course.save()

        messages.success(request, 'Course added successfully.')
        return redirect('course_view')

    # If the request method is not POST, render the course.html template with existing data
    courses = courseModel.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course.html', context)

def books_view(request):
    if request.method == "POST":
        books_name = request.POST.get('books_name')
        written_by = request.POST.get('written_by')
        book_pages = request.POST.get('book_pages')

        # Validate the data (add more validation as needed)
        if not books_name or not written_by or not book_pages:
            messages.error(request, 'Please fill in all fields.')
            return redirect('books_view')

        # Create a new booksModel instance
        new_book = booksModel.objects.create(
            books_name=books_name,
            written_by=written_by,
            book_pages=book_pages
        )

        # Save the new book instance
        new_book.save()

        messages.success(request, 'Book added successfully.')
        return redirect('books_view')

    # If the request method is not POST, render the books.html template with existing data
    books = booksModel.objects.all()
    context = {
        'book': books
    }
    return render(request, 'books.html', context)


def profile_view(request):
     return render(request, 'profile.html')

