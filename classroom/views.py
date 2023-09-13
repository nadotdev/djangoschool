from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from classroom.forms import GradeForm, SubjectForm
from classroom.models import Grade, Subject
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

# Create your views here.
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
    
    
  
def create_subject(request) :
    
    if request.method == "POST":
        print('DD::: Create subject works.')

    
    return render(request, 'classroom/subjects/assign.html')



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

