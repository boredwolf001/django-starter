from django.shortcuts import render, redirect
from django.contrib.auth import login as log_in, logout as log_out, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import ProfileForm
from . import models


def home(request):
      return render(request, 'pages/home.html')


def login(request):
      if request.user.is_authenticated:
            return redirect('base:profile')

      if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                  log_in(request, user)
                  return redirect('base:profile')
            else:
                  return redirect('base:login')

      return render(request, 'registration/login.html')


@login_required(login_url='base:login')
def profile(request):
      return render(request, 'registration/profile.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('base:profile')

    if request.method == 'POST':
      uform = UserCreationForm(request.POST)
      pform = ProfileForm(request.POST, request.FILES)
      
      if uform.is_valid() and pform.is_valid():
            user = uform.save()

            profile = pform.save(commit=False)
            profile.user = user
            profile.save()
            
            return redirect('base:login')
      
      else:
            return render(request, 'registration/register.html', {'uform': uform, 'pform': pform, 'errors': ['Form not valid']})

    uform = UserCreationForm()
    pform = ProfileForm()
    return render(request, 'registration/register.html', {'uform': uform, 'pform': pform})

def logout(request):
      log_out(request)

      return redirect('base:login')