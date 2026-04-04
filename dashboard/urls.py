from .views import dashboard, register,register_hours
from django.urls import path

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('registers/', register, name="registers"),
    path('registers/create', register_hours, name="register_create"),

]