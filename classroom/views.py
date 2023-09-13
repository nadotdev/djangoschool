from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from classroom.forms import GradeForm, SubjectForm
from classroom.models import Grade, Subject, Teacher
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


def assign_grades(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            grade_name = request.POST.get('grade_name')
            data = Grade(grade_name=grade_name)
            data.save()
            messages.success(request, 'Grade has been assigned.')
            return HttpResponseRedirect('/classroom/grades')
    else: 
        form = GradeForm()
    return render(request, 'classroom/grades/assign.html', {'form': form})


def grades(request):
    """Retrieved grades list

    Args:
        request (_type_): _description_
    """
    grade_list = Grade.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(grade_list, 5)
    try:
        grade_list = paginator.page(page)
    except PageNotAnInteger:
        grade_list = paginator.page(1)
    except EmptyPage:
        grade_list = paginator.page(paginator.num_pages)
    context = {'grade_list': grade_list}
    
    return render(request, 'classroom/grades/index.html', context)
    
    
def modify_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == "POST":
        grade.grade_name = request.POST.get('grade_name')
        grade.save()
        messages.success(request, 'Grade modified.')
        return HttpResponseRedirect("/classroom/grades")
    
    return render(request, 'classroom/grades/modify.html', {'grade': grade})


def delete(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == "POST":
        grade.delete()
        messages.success(request, 'Grade destroyed.')
        return HttpResponseRedirect("/classroom/grades")

  
def create_subject(request):
    grade_list = Grade.objects.all()
    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        grade_id = request.POST.get('grade_id')
        data = Subject(subject_name=subject_name, grade_id=grade_id)
        data.save()
        messages.success(request, 'Subject has assigned to grade.')
        return HttpResponseRedirect('/classroom/subjects')
    context = {
        'grades': grade_list
    }
    return render(request, 'classroom/subjects/create_subject.html', context)


def subjects(request):
    """ List data to templates."""
    subject_list = Subject.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(subject_list, 5)
    try:
        subject_list = paginator.page(page)
    except PageNotAnInteger:
        subject_list = paginator.page(1)
    except EmptyPage:
        subject_list = paginator.page(paginator.num_pages)
    context = {'subject_list': subject_list}
    
    return render(request, 'classroom/subjects/index.html', context)


def modify_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    grade_list = Grade.objects.all()
    if request.method == "POST":
        subject.subject_name = request.POST.get('subject_name')
        subject.grade_id = request.POST.get('grade_id')
        subject.save()
        messages.success(request, 'Subject has modified.')
        return HttpResponseRedirect('/classroom/subjects')
    context = {'subject': subject, 'grades': grade_list}
    return render(request, 'classroom/subjects/modify.html', context)


def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == "POST":
        subject.delete()
        messages.warning(request, 'Subject has been deleted.')
        return HttpResponseRedirect('/classroom/subjects')


# Teacher view
def get_all_teacher(request):
    """ Retrieve all teacher data"""
    teacher_list = Teacher.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(teacher_list, 5)
    try:
        teacher_list = paginator.page(page)
    except PageNotAnInteger:
        teacher_list = paginator.page(1)
    except EmptyPage:
        teacher_list = paginator.page(paginator.num_pages)
    context = {'teacher_list': teacher_list}
    return render(request, 'classroom/teachers/index.html', context)


def create_teacher(request):
    if request.method == "POST":
        name = request.POST.get('teacher_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        if 'photo' in request.FILES:
            photo = request.FILES.get('photo')
        else:
            photo = None
        data = Teacher(
            name=name,
            phone=phone,
            email=email,
            dob=dob,
            photo=photo
        )
        data.save()
        messages.success(request, 'Teacher has been enrolled successful.')
        return HttpResponseRedirect('/classroom/teachers')
    return render(request, 'classroom/teachers/create_teacher.html')
