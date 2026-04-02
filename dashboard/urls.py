from .views import dashboard, register_hours
from django.urls import path

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('register/', register_hours, name="register_hours"),

]