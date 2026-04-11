from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Topic, Student, Register
from .serializers import TopicSerializer, RegisterSerializer
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum

class DataHours(APIView):
    # future otimization(performance)
    # future otimization(querys)
    def get(self, request, pk=None):
        if pk:
            user_id = pk
        else:
            user_id = request.user.id

        # today
        today = timezone.now().date()
        print(today)
        register_today = Register.objects.filter(student__user_id=user_id, created_at__date=today)
        today_hours = sum(r.hours for r in register_today)

        # weekly
        weekly = today.weekday()
        # monday = 0
        # third = 1
        # ...
        # sunday = 6

        days_since_sunday = (weekly + 1) % 7
        last_sunday = today - timedelta(days=days_since_sunday)
        print(last_sunday)

        register_weekly = Register.objects.filter(
            student__user_id=user_id,
            created_at__date__gte=last_sunday,
            created_at__date__lte=today
        )

        weekly_hours = sum(r.hours for r in register_weekly)

        # total
        total_hours = Student.objects.get(user_id=user_id).total_hours
        print(total_hours)

        return Response({"today": today_hours, "weekly": weekly_hours, "total": total_hours})

class DataRegister(APIView):
    def get(self, request):
        order = request.GET.get('desc')
        get_all = request.GET.get('all')

        order = "id" if order else "-id"
            
        registers = Register.objects.order_by(order)[:10] if not get_all else Register.objects.order_by(order)
        
        serializer = RegisterSerializer(registers, many=True)

        print(registers, serializer)

        return Response(serializer.data)
    
class DataRegisterPersonal(APIView):
    def get(self, request, pk=None):
        order = request.GET.get('desc')
        get_all = request.GET.get('all')

        if pk:
            user_id = pk
        else:
            user_id = request.user.id

        order = "-id" if order else "id"

        registers = Register.objects.filter(student__user_id=user_id).order_by(order)[:10] \
            if not get_all else \
                    Register.objects.filter(student__user_id=user_id).order_by(order)
        
        serializer = RegisterSerializer(registers, many=True)

        print(registers, serializer)

        return Response(serializer.data)
    
    def post(self, request, pk):
        topic_name = request.data.get("topic")
        hours = request.data.get("hours")

        # possible error(not user.id)
        if pk:
            user_id = pk
        else:
            user_id = request.user.id

        student = Student.objects.get(user_id=user_id)
        topic = Topic.objects.get(name=topic_name)

        student.total_hours += int(hours)
        student.save()

        topic.hours += int(hours)
        topic.save()

        Register.objects.create(student=student, topic=topic, hours=hours)

        return Response({})


class DataTopic(APIView):
    def get(self, request, pk=None):
        rank = request.GET.get('rank')

        if pk:
            user_id = pk
        else:
            user_id = request.user.id

        topics = Topic.objects.filter(student__user_id=user_id).order_by("-hours")[:4] \
            if rank else Topic.objects.filter(student__user_id=user_id)

        serializer = TopicSerializer(topics, many=True)

        return Response(serializer.data)

    def post(self, request, pk=None):
        topic_name = request.data.get("name")
        topic_color = request.data.get("color")

        if pk:
            user_id = pk
        else:
            user_id = request.user.id

        student = Student.objects.get(user_id=user_id)

        Topic.objects.create(student=student, name=topic_name, color=topic_color)

        return Response({})
    
    def put(self, request, pk=None): # try exception future aditions
        topic_id = request.data.get("id")
        name = request.data.get("name")
        color = request.data.get("color")

        if pk:
            user_id = pk
        else:
            user_id = request.user.id

        topic = Topic.objects.get(id=topic_id, student__user_id=user_id)

        if name:
            topic.name = name
        
        if color:
            topic.color = color

        topic.save()

        return Response({}) # returns future something
    
    def delete(self, request, pk=None):
        topic_id = request.data.get("id") # possible error(not name)

        if pk:
            user_id = pk
        else:
            user_id = request.user.id
        
        student = Student.objects.get(user_id=user_id)
        topic = Topic.objects.get(id=topic_id)

        student.total_hours -= int(topic.hours)
        student.save()

        topic.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class WeeklyDataHours(APIView):
    def get(self, request):

        today = timezone.now().date()

        start_week = today - timedelta(days=today.weekday())
        print(start_week)

        registers = Register.objects.filter(
            created_at__date__gte=start_week,
            see=True
        ).values("created_at__week_day").annotate(total=Sum("hours"))
        print(registers)

        week_data = {i: 0 for i in range(1, 8)}
        for r in registers:
            week_data[r["created_at__week_day"]] = r["total"]

        # organiza Segunda → Domingo
        labels = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]

        data = [week_data[i] for i in range(1, 8)]

        print(data)

        return Response({
            "labels": labels,
            "data": data
        })