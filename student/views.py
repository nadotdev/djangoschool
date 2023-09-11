from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from student.forms import ParentForm
from student.models import Parent
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def student_enrollment(request):
    parent_id = Parent.objects.all()
    context = {'parent_id': parent_id}
    return render(request, 'students/enrollment.html', context)


def register_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            parent_of = request.POST.get('parent_of')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            # save to database
            data = Parent(
                parent_of_student=parent_of,
                phone=phone,
                email=email)
            data.save()
            messages.success(request, 'Parent registered.')
            return HttpResponseRedirect('/student/parents')
    else:
        form = ParentForm()
    return render(request, 'parent/register.html', {'form': form})


def parents(request):
    """ Parent Listing """
    parent_list = Parent.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(parent_list, 5)
    try:
        parent_list = paginator.page(page)
    except PageNotAnInteger:
        parent_list = paginator.page(1)
    except EmptyPage:
        parent_list = paginator.page(paginator.num_pages)

    context = {'parents': parent_list}
    return render(request, 'parent/parents.html', context)


def delete_parent_by_id(request, pid):
    """deleting student's parent by their id"""

    parent = get_object_or_404(Parent, id=pid)
    if request.method == 'POST':
        if parent:
            parent.delete()
            messages.success(request, 'Parent deleted.')
            return HttpResponseRedirect('/student/parents')
        else:
            messages.error(request, 'An error occurred while deleting.')


def modify_parent(request, pid):
    """ modify_parent student's parent by their id
        bring value to form for make changes
    """

    parent = Parent.objects.filter().get(id=pid)
    context = {'parent': parent}
    return render(request, 'parent/modify.html', context)


def update_parent(request, pid):
    """
        update student's parent
        and save to database
    """
    parent = get_object_or_404(Parent, id=pid)

    if request.method == 'POST':
        parent.parent_of_student = request.POST.get('parent_of')
        parent.phone = request.POST.get('phone')
        parent.email = request.POST.get('email')

        # Save the updated parent information
        parent.save()
        messages.success(request, 'Parent Updated.')
        return HttpResponseRedirect('/student/parents')


def search_parent_by_phone(request, p_phone):
    """ Search and return parent info"""

