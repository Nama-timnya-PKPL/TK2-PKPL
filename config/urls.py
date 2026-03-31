from django.contrib import admin
from django.urls import path
from main.views import home, login_view ,register_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]