from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('properties/', views.PropertyBrowser.as_view(), name='properties'),
    path('viewing/<int:propery_id>', views.Viewing.as_view(), name='viewing'),
    path('accounts/', include('main_app.urls_auth')),
]
