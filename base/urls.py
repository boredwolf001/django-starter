from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('auth/register', views.register, name='register'),
    path('auth/login', views.login, name='login'),
    path('auth/profile', views.profile, name='profile'),
    path('auth/logout', views.logout, name='logout'),
]
