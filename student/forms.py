from django import forms

from student.models import Parent


class ParentForm(forms.Form):
    class Meta:
        model = Parent
        fields = "__all__"
