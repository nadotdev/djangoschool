from django import forms

from student.models import Parent, Student, Attendance


class ParentForm(forms.Form):
    class Meta:
        model = Parent
        fields = "__all__"


class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = "__all__"


class AttendanceForm(forms.Form):
    class Meta:
        model = Attendance
        fields = "__all__"


