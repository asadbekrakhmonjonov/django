from django.urls import path
from . import views
urlpatterns = [
    path('', views.endpoints),
    path('advocate/', views.advocate_list),
    path('advocates/<str:username>/', views.advocate_detail),
]
