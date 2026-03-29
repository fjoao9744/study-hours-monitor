from .views import dashboard, register_hours, add_topic, remove_topic
from django.urls import path

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('register/', register_hours, name="register_hours"),
    path('add_topic/', add_topic, name='add_topic'),
    path('delete_topic/', remove_topic, name='remove_topic'),

]