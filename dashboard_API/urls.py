from django.urls import path
from .views import DataHours, DataRegister, DataRegisterDetail, DataTopic, WeeklyDataHours

urlpatterns = [
    path('hours/', DataHours.as_view()),
    path('hours/<int:pk>/', DataHours.as_view()),

    path('register/', DataRegister.as_view()),
    path('register/<int:pk>/', DataRegisterDetail.as_view()),
    
    path('topic/', DataTopic.as_view()),
    path('topic/<int:pk>/', DataTopic.as_view()),

    path('graphs/weekly/hours/', WeeklyDataHours.as_view())
]