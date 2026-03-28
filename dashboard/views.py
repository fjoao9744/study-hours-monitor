from django.shortcuts import render, redirect
from .models import Topic, Student, Register
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "index.html")

@login_required
def register_hours(request):
    if request.method == "POST":
        topic = request.POST["topic"]
        hours = request.POST["hours"]
        student = Student.objects.create(user=request.user, total_hours=hours)
        if not Topic.objects.filter(name=topic).exists():
            topic = Topic.objects.create(name=topic)
        else:
            topic = Topic.objects.get(name=topic)
        Register.objects.create(student=student, topic=topic, hours=hours)

        return redirect("dashboard")

    return render(request, "register_hours.html")