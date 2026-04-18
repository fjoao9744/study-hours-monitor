from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    total_hours = models.IntegerField()

    class Meta:
        db_table = "students"

    def __str__(self):
        return self.user.username

class Topic(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=100, null=False)
    hours = models.DecimalField(default=0, max_digits=4, decimal_places=2, null=False)
    color = models.CharField(default="#4E4E4E", max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "topics"
        unique_together = ['student', 'name']

    def __str__(self):
        return self.name
    
class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registers')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    hours = models.FloatField(null=False)
    commentary = models.CharField(default="", max_length=255, blank=True)
    see = models.BooleanField(default=True)
    feedback = models.IntegerField(default=-1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "registers"

    def __str__(self):
        return f"{self.student} - {self.hours}h"