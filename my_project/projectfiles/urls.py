from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('user_info/', views.userInfo, name='user_info'),
    path('task_info/', views.taskInfo, name='task_info'),
    path('task_list'
         '/', views.taskList, name='task_list'),


]
