from django.db import models


class Parent(models.Model):
    """
         Parent model fields
     """
    parent_of_student = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateField(auto_now=True)


class Student(models.Model):
    """
    Student model fields
    """
    firstname = models.CharField(max_length=25, null=False)
    lastname = models.CharField(max_length=25, null=False)
    gender = models.IntegerField()
    date_of_birth = models.DateField(null=False)
    date_of_joined = models.DateField(null=False)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/', null=True)
    created_at = models.DateField(auto_now=True)


class Attendance(models.Model):
    """
        Remark store 0, 1, 2 (0=P, 1=L, 2=A)
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    remark = models.IntegerField()
    created_at = models.DateField(auto_now=True)

