from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')
    total_hours = models.IntegerField()
    def __str__(self):
        return self.user.username

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registers')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    hours = models.FloatField()

    def __str__(self):
        return f"{self.student} - {self.hours}h"