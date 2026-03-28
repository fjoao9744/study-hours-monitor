from django.shortcuts import render
from .models import Topic

def dashboard(request):
    Topic.objects.create(name="test")
    return render(request, "index.html")
