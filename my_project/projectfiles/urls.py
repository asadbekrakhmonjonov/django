from django.urls import path
from .import views
from .views import *
urlpatterns = [
    path('', views.signPage),
    path('home/', views.homePage),
    path('task_page/', views.taskPage, name="task_page"),
    path('updateTask/<int:pk>/', views.updateTask, name="updateTask"),
]