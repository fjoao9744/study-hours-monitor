from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Topic, Student, Register
from .serializers import TopicSerializer
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

# DataRegister
    # post: hours_total | topic.hours
# DataTopic
    # add_topic(post)
    # remove_topic(delete)
