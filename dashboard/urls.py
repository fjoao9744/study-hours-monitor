from .views import dashboard, registers, registers_create, topics
from django.urls import path

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('registers/', registers, name="registers"),
    path('registers/create/', registers_create, name="registers_create"),
    path('topics/', topics, name="topics"),

]