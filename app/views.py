from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from classroom.models import ClassroomModel, Teacher
from student.models import Student, Parent


@login_required
def dashboard(request):
    total_student = Student.objects.count()
    total_teacher = Teacher.objects.count()
    total_parent = Parent.objects.count()
    total_classroom = ClassroomModel.objects.count()
    

    print(total_student)
    context = {
        'total_student': total_student,
        'total_teacher': total_teacher,
        'total_parent': total_parent,
        'total_classroom': total_classroom,
        
    }
    return render(request, 'dashboard/index.html', context)

