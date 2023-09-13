
from django.urls import path
from classroom import views
urlpatterns = [
    path('assign-grades/', views.assign_grades, name="classroom-assign-grade"),
    path('grades/', views.grades, name="classroom-list-grade"),
    path('modify-grade/<int:grade_id>', views.modify_grade, name="classroom-modify-grade"),
    path('delete-grade/<int:grade_id>', views.delete, name="classroom-delete-grade"),
    
    path('create-subject/', views.create_subject, name="classroom-create-subject"),
    path('subjects/', views.subjects, name="classroom-list-subject"),
    path('modify-subject/<int:subject_id>', views.modify_subject, name="classroom-modify-subject"),
    path('delete-subject/<int:subject_id>', views.delete_subject, name="classroom-delete-subject"),

    path('teachers/', views.get_all_teacher, name="classroom-list-teacher"),
    path('enroll-teachers/', views.create_teacher, name="classroom-create-teacher"),
    path('delete-teacher/<int:teacher_id>', views.delete_teacher_record, name="classroom-delete-teacher"),
    path('modify-teacher/<int:teacher_id>', views.modify_teacher_record, name="classroom-modify-teacher"),

]
