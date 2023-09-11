from django.db import models


class Parent(models.Model):
    parent_of_student = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateField(auto_now=True)

