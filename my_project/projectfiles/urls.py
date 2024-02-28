from django.urls import path
from .import views
from .views import *
urlpatterns = [
    path('', views.signPage),
    path('home/', views.homePage),
    path('task_page/', views.taskPage, name="task_page"),
    path('update_task/<str:pk_test>/', views.updateTask, name="update_task"),
    path('deleteTask/<str:pk>/', views.deleteTask, name="delete_task"),
]