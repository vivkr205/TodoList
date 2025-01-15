from django.shortcuts import render,redirect
from .forms import CustomRegistration
from django.contrib import messages
from django.views import View
from django.contrib.auth import logout

# Create your views here.


def home(request):
    register_form = CustomRegistration()
    if request.method=="POST":
        register_form=CustomRegistration(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,('New User Account Created, Let get Login!'))
            return redirect('register')   
    else:
        register_form=CustomRegistration()
    return render(request,'register.html',{'register_form':register_form})

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return render(request,'logout.html')