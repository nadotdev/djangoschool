from django.db import models

# Create your models here.
class Grade(models.Model):
    """ For grade model. e.g: 12A, 12B"""
    
    grade_name = models.CharField(max_length=25, null=False)
    
class Subject(models.Model):
    
    subject_name = models.CharField(max_length=20, null=False)
    grade = models.ForeignKey(Grade, related_name='grade_id', on_delete=models.CASCADE, default=1)

        
    