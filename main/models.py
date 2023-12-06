from django.db import models
from main.utils.constant import PERMISSIONS

# Create your models here.
class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class courseModel(baseModel):
    course_name = models.CharField(max_length=100)
    course_faculaty_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=50)
    course_fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.course_name
    
class studentModel(baseModel):
    first_name = models.CharField(max_length=255, null=False, blank= False)
    last_name = models.CharField(max_length=255, null=False, blank= False)
    email = models.EmailField(max_length=255, null=False, blank= False, unique= True)
    mobile = models.CharField(max_length=20, null=False, blank= False, unique= True)
    course_name = models.ForeignKey(courseModel, on_delete=models.CASCADE,related_name='students_course_name')
    status = models.CharField(default='Pending', max_length=50, choices=PERMISSIONS)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class teachersModel(baseModel):
    first_name = models.CharField(max_length=255, null=False, blank= False)
    last_name = models.CharField(max_length=255, null=False, blank= False)
    email = models.EmailField(max_length=255, null=False, blank= False, unique= True)
    mobile = models.CharField(max_length=20, null=False, blank= False, unique= True)
    course = models.CharField(max_length=255, null=False, blank= False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - { self.course}"
    


    

class booksModel(baseModel):
    books_name = models.CharField(max_length=100)
    written_by = models.CharField(max_length=100)
    book_pages = models.PositiveIntegerField()
    
    def __str__(self):
        return self.books_name

    

