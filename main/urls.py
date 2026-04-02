from django.urls import path
from .views import home
from main import views

urlpatterns = [
     path('', home, name='home'),
    path('logout/', views.logout_then_login, name='custom_logout'),
    

]
