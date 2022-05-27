from . import views_auth
from django.urls import path

urlpatterns = [
    path('login/', views_auth.Login.as_view(), name='login'),
    path('logout/', views_auth.Logout.as_view(), name='logout'),
    path('register/', views_auth.Register.as_view(), name='register'),
]
