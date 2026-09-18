from . import views
from django.urls import path 

urlpatterns = [
    path('home/', views.home, name='home'),
    path('task/<slug:slug>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<slug:slug>/update/', views.task_update, name='task_update'),
    path('task/<slug:slug>/delete/', views.task_delete, name='task_delete'),
]