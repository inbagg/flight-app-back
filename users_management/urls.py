from django.urls import path
from . import views

urlpatterns = [
    path('users_management/', views.roles),

    path('administrators/', views.administrators, name="administrators"),
    path('administrators/<str:pk>/', views.administrators, name="administrators"),
    path('create-administrator/', views.createAdministrator, name='create-administrator'),
    path('update-administrator/<str:pk>/', views.updateAdministrator, name='update-administrator'),
    path('delete-administrator/<str:pk>/', views.deleteAdministrator, name='delete-administrator'),

    path('roles/', views.roles, name="roles"),
    path('roles/<str:pk>/', views.roles, name="roles"),
    path('create-role/', views.createRole, name='create-role'),
    path('update-role/<str:pk>/', views.updateRole, name='update-role'),
    path('delete-role/<str:pk>/', views.deleteRole, name='delete-role'),
]