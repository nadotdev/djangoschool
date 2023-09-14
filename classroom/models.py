from django.db import models
from student.models import Student

default_no_image = "https://firebasestorage.googleapis.com/v0/b/fir-64ff1.appspot.com/o/user.png?alt=media&token=2d2e18cb-8019-4e0d-b215-1f4ed4b85ba9"


class Grade(models.Model):
    """ For grade model. e.g: 12A, 12B"""
    
    grade_name = models.CharField(max_length=25, null=False)


class Subject(models.Model):
    
    subject_name = models.CharField(max_length=20, null=False)
    grade = models.ForeignKey(Grade, related_name='grade_id', on_delete=models.CASCADE, default=1)


class Teacher(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    dob = models.DateField()
    phone = models.CharField(max_length=25, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True, default="teacher-email@industry.com")
    photo = models.ImageField(upload_to='uploads/', null=True)
    created_at = models.DateField(auto_now=True)

class ClassroomModel(models.Model):
    room_number = models.CharField(max_length=5, null=False)
    year = models.DateField()
    grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    