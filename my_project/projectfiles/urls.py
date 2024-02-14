from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('user_info/', views.userInfo, name='user_info'),

]