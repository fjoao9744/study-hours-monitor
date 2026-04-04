from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):

    return render(request, "dashboard/dashboard.html")

@login_required
def register(request):
    return render(request, "dashboard/register.html")

@login_required
def register_hours(request):

    return render(request, "dashboard/register_hours.html")

