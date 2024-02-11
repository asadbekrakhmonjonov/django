from . import views
from django.urls import path
urlpatterns = [
    path('', views.main),
    path('product/', views.product),
    path('customer/<str:pk_test>/', views.customer),

]
