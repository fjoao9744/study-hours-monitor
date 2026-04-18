from django.urls import path
from .views import DataHours, DataRegister, DataRegisterDetail, DataTopic, WeeklyDataHours, WeeklyDataHoursUser

urlpatterns = [
    path('hours/', DataHours.as_view()),
    path('hours/<int:pk>/', DataHours.as_view()),

    path('register/', DataRegister.as_view()),
    path('register/user/', DataRegisterDetail.as_view()),
    path('register/user/<int:pk>/', DataRegisterDetail.as_view()),
    
    path('topic/', DataTopic.as_view()),
    path('topic/<int:pk>/', DataTopic.as_view()),

    path('graphs/weekly/hours/', WeeklyDataHours.as_view()),
    path('graphs/weekly/hours/user/', WeeklyDataHoursUser.as_view()),
    path('graphs/weekly/hours/user/<int:pk>', WeeklyDataHoursUser.as_view()),
]