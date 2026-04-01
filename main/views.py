from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse


def home(request):
    return render(request, 'pages/home.html', {
    })
def login_view(request):
    return render(request, 'pages/login.html')


def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Password tidak sama!")
            return redirect("register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email sudah terdaftar!")
            return redirect("register")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password1,
            first_name=name
        )

        messages.success(request, "Akun berhasil dibuat!")
        return redirect("login")

    return render(request, "pages/register.html")
