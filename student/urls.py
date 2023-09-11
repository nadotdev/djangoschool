from django.contrib import admin
from django.urls import path, include
from student import views

urlpatterns = [
    path('enrollment/', views.student_enrollment, name='student-enrollment'),


    path('parent/', views.register_parent, name='parent-register'),
    path('parents/', views.parents, name='parent-list'),
    path('parents/<int:pid>', views.delete_parent_by_id, name='parent-delete'),
    path('parents/modifying/<int:pid>', views.modify_parent, name='parent-modify'),
    path('parents/update/<int:pid>', views.update_parent, name='parent-update'),

]
