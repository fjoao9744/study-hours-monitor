from .views import dashboard, registers, topics
from django.urls import path

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('registers/', registers, name="registers"),
    path('topics/', topics, name="topics"),

]