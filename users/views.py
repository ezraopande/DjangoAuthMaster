from django.http import request
from django.shortcuts import render, redirect

from django.views.generic import CreateView
from users.models import CustomUser
from users.form import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth/signup.html'


class UserLoginPageView(LoginView):
    template_name = 'auth/login.html'

@login_required
def home(request):
    return render(request, 'home.html')


def Logout(request):
    logout(request)
    return redirect('login')
