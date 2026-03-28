from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic, Student, Register
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

@login_required
def register_hours(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        topic = request.POST["topic"]
        hours = request.POST["hours"]

        Register.objects.create(student=student, topic=topic, hours=hours)

        return redirect("dashboard")
    
    topics = Topic.objects.filter(student_id=student)
    print(topics)

    return render(request, "dashboard/register_hours.html", {"topics": topics})

def add_topic(request):
    student = Student.objects.get(user=request.user)
    topico = request.POST["topic"]
    topico = topico.strip().lower()
    print(topico)
    Topic.objects.create(student=student, name=topico)
    return HttpResponse("Topico criado")

def delete_topic(request):
    student = Student.objects.get(user=request.user)
    topico = request.POST["topic"]
    topico = topico.strip().lower()
    print(topico)
    Topic.objects.get(student=student, name=topico).delete()
    return HttpResponse("Topico deletado")