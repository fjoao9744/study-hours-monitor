from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from dashboard_API.models import Student
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Teste",
            "Funcionando!",
            "site@gmail.com",
            ["user@gmail.com"]
        )
        Student.objects.create(user=instance, total_hours=0)