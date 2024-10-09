from django.shortcuts import render

def register_view(request):
    return  render(request, 'auth/register/register.html')

def login_view(request):
    return  render(request, 'auth/login/login.html')

def profile_view(request):
    return  render(request, 'profile/profile.html')
