from django.urls import path
from .views import DataHours

urlpatterns = [
    path('hours/', DataHours.as_view()),
    path('hours/<int:pk>/', DataHours.as_view()),
]