from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Topic, Student, Register
from .serializers import TopicSerializer, RegisterSerializer
from django.utils import timezone
from datetime import timedelta

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

        topics = Topic.objects.filter(student__user_id=user_id).order_by("-hours") \
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
    
    def delete(self, request, pk):
        topic_name = request.data.get("name") # possible error(not name)

        if pk:
            user_id = pk
        else:
            user_id = request.user.id
        
        student = Student.objects.get(user_id=user_id)
        topic = Topic.objects.get(name=topic_name)

        student.total_hours -= int(topic.hours)
        student.save()

        topic.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    