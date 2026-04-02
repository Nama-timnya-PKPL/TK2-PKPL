from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings

def home(request):
    show_theme = (
        request.user.is_authenticated and 
        request.user.email in settings.THEME_ALLOWED_EMAILS
    )
    return render(request, 'pages/home.html', {'show_theme': show_theme})

def logout_then_login(request):
    logout(request)
    return redirect('account_login')  

