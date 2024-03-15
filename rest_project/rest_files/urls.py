from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('', views.Endpoints.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('advocates/', views.AdvocateList.as_view()),
    path('advocate/<str:username>/', views.AdvocateDetail.as_view()),
    path('companies/', views.CompaniesList.as_view()),

]
