from django.shortcuts import render
from dashboard_API.models import Topic, Register
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

@login_required
def registers(request):
    registers = Register.objects.filter(student__user_id=request.user.id).order_by('-created_at')
    topics = Topic.objects.filter(student__user_id=request.user.id)
    return render(request, "dashboard/registers.html", {"registers": registers, "topics": topics})

@login_required
def topics(request):
    topics = Topic.objects.filter(student__user_id=request.user.id)
    return render(request, "dashboard/topics.html", {"topics": topics})

@login_required
def teste(request):
    return render(request, "dashboard/teste.html")

