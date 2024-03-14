from django.urls import path
from . import views
urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocate_list, name='advocates'),
    path('advocate/<str:username>/', views.AdvocateDetail.as_view()),
]
