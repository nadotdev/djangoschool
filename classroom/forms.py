from django import forms
from classroom.models import Grade, Subject

class GradeForm(forms.ModelForm):
    
    class Meta:
        model = Grade
        fields = '__all__'
        
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'