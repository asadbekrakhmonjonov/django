from django.urls import path
from .import views
from .views import *
urlpatterns = [
    path('', views.signPage),
    path('home/', views.homePage),
    path('task/', views.taskPage),
    path('updateTask/<int:pk>/', views.updateTask, name="updateTask"),
]