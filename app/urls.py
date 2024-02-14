from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import CustomLogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('register', views.register, name='register'),
    path('generate_password', views.generate_password, name='generate_password'),
]
