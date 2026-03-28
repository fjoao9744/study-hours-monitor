from .views import dashboard, register_hours, add_topic, delete_topic
from django.urls import path

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('register/', register_hours, name="register_hours"),
    path('add_topic/', add_topic),
    path('delete_topic/', delete_topic),

]