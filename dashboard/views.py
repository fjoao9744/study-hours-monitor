from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic, Student, Register
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    student = Student.objects.get(user=request.user)

    topics = Topic.objects.filter(student=student)
    registers = Register.objects.filter(student=student)

    for topic in topics:
        print(topic.name)

    return render(request, "dashboard/dashboard.html", {"topics": topics, "registers": registers})

@login_required
def register_hours(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        topic = request.POST["topic"]
        hours = request.POST["hours"]

        topic = Topic.objects.get(student=student, name=topic)
        topic.hours += int(hours)
        topic.save()

        student.total_hours += int(hours)
        student.save()

        Register.objects.create(student=student, topic=topic, hours=hours)

        return redirect("dashboard")
    
    topics = Topic.objects.filter(student_id=student)
    print(topics)

    return render(request, "dashboard/register_hours.html", {"topics": topics})

# API change
def add_topic(request):
    student = Student.objects.get(user=request.user)
    topic = request.POST["new_topic"]
    color = request.POST["color"]
    print(topic)
    Topic.objects.create(student=student, name=topic, color=color)
    return redirect("dashboard")

def remove_topic(request):
    topic = request.POST["topic"]
    print(topic)
    Topic.objects.get(id=topic).delete()
    return redirect("dashboard")