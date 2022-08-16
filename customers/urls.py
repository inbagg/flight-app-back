from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('users', views.CustomerCreate.as_view(), name="users"),
    path('customers/', views.customers, name="customers"),
    path('customers/<str:pk>/', views.customers, name="customers"),
    path('create-customer/', views.createCustomer, name='create-customer'),
    path('update-customer/<str:pk>/',
         views.updateCustomer, name='update-customer'),
    path('delete-customer/<str:pk>/',
         views.deleteCustomer, name='delete-customer'),
    path('token/obtain', views.MyTokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login', TokenObtainPairView.as_view()),
]
