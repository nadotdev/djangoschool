
from django.contrib import admin
from django.urls import path, include
from student import views

urlpatterns = [
    path('enrollment/', views.student_enrollment, name='student-enrollment'),
    path('listing/', views.student_list, name='student-list'),
    path('modifying/<int:sid>', views.modify_student, name='student-modify'),
    path('update/<int:sid>', views.update_student, name='student-update'),

    path('parent/', views.register_parent, name='parent-register'),
    path('parents/', views.parents, name='parent-list'),
    path('parents/<int:pid>', views.delete_parent_by_id, name='parent-delete'),
    path('parents/modifying/<int:pid>', views.modify_parent, name='parent-modify'),
    path('parents/update/<int:pid>', views.update_parent, name='parent-update'),

    path('attendances/', views.attendance_list, name='student-attendance-list'),
    path('create-attendance/', views.create_attendance, name='create-attendance'),
    path('modify-attendance/<int:attendance_id>', views.modify_attendance, name='modify-attendance'),
    path('delete-attendance/<int:attendance_id>', views.delete_attendance, name='delete-attendance'),

]
