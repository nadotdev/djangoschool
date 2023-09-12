from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from student.forms import ParentForm, StudentForm, AttendanceForm
from student.models import Parent, Student, Attendance
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def student_enrollment(request):
    parent_id = Parent.objects.all()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            date_joined = request.POST.get('date_joined')
            parent_id = request.POST.get('parent_id')
            photo = request.FILES.get('photo')

            data = Student(
                firstname=firstname,
                lastname=lastname,
                gender=gender,
                date_of_birth=dob,
                date_of_joined=date_joined,
                parent_id=parent_id,
                photo=photo
            )
            data.save()
            messages.success(request, 'Student has been registered successful.')
            return HttpResponseRedirect('/student/listing')

    else:
        form = StudentForm()
    context = {
        'parent_id': parent_id,
        'form': form
    }
    return render(request, 'students/enrollment.html', context)


def student_list(request):
    students = Student.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(students, 4)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    context = {'students': students}
    return render(request, 'students/student_list.html', context)


def modify_student(request, sid):
    """ modify_parent student's parent by their id
        bring value to form for make changes
    """
    student = Student.objects.filter().get(id=sid)
    parent_id = Parent.objects.all()

    context = {
        'student': student,
        'parent_id': parent_id
    }
    return render(request, 'students/modify.html', context)


def update_student(request, sid):
    student = get_object_or_404(Student, id=sid)
    if request.method == "POST":
        student.firstname = request.POST.get('new_firstname')
        student.lastname = request.POST.get('new_lastname')
        student.gender = request.POST.get('new_gender')
        student.date_of_birth = request.POST.get('new_dob')
        student.date_joined = request.POST.get('new_date_joined')
        student.parent_id = request.POST.get('new_parent_id')
        if 'new_photo' in request.FILES:
            student.photo = request.FILES['new_photo']
        student.save()
        messages.success(request, 'Student Updated.')
        return HttpResponseRedirect('/student/listing')


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


def attendance_list(request):
    """ List of attendance"""
    attendances = Attendance.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(attendances, 4)
    try:
        attendances = paginator.page(page)
    except PageNotAnInteger:
        attendances = paginator.page(1)
    except EmptyPage:
        attendances = paginator.page(paginator.num_pages)

    context = {'attendances': attendances}
    return render(request, 'students/attendance.html', context)


def create_attendance(request):
    students = Student.objects.all()
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            date = request.POST.get('date')
            remark = request.POST.get('remark')
            student_id = request.POST.get('student_id')

            form_fields = Attendance(
                date=date,
                remark=remark,
                student_id=student_id
            )
            form_fields.save()
            messages.success(request, 'Attendance marked.')
            return HttpResponseRedirect('/student/attendances')
    else:
        form = AttendanceForm()
    context = {
        'form': form,
        'students': students
    }
    return render(request, 'students/create_attendance.html', context)


def modify_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    student = attendance.student
    if request.method == "POST":
        # attendance.date = request.POST.get('date')
        attendance.remark = request.POST.get('remark')
        attendance.save()
        messages.success(request, 'Attendance modified.')
        return HttpResponseRedirect('/student/attendances')

    context = {'student': student, 'attendance': attendance}
    return render(request, 'students/modify_attendance.html', context)


def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    if request.method == 'POST':
        if attendance:
            attendance.delete()
            messages.success(request, 'Attendance deleted.')
            return HttpResponseRedirect('/student/attendances')
        else:
            messages.error(request, 'An error occurred while deleting.')
