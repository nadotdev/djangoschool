
from django.urls import path
from classroom import views
urlpatterns = [
    path('assign-grades/', views.assign_grades, name="classroom-assign-grade"),
    path('grades/', views.grades, name="classroom-list-grade"),
    path('modify-grade/<int:grade_id>', views.modify_grade, name="classroom-modify-grade"),
    path('delete-grade/<int:grade_id>', views.delete, name="classroom-delete-grade"),
    
    path('create-subject/', views.create_subject, name="classroom-create-subject"),
    path('subjects/', views.subjects, name="classroom-list-subject"),

    
]