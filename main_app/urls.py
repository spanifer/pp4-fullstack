from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('property-browser/', views.PropertyBrowser.as_view(), name='properties'),
]
