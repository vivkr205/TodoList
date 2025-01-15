from django.urls import path
from userApp import views 
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView


urlpatterns = [
    
    path('register',views.home,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
