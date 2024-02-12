from . import views
from django.urls import path
urlpatterns = [
    path('', views.main, name="home"),
    path('product/', views.product, name="product"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<int:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<int:pk>/', views.deleteOrder, name="delete_order"),
]
