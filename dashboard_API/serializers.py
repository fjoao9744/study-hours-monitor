from rest_framework import serializers
from .models import Topic, Register

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    topic_name = serializers.CharField(source='topic.name', read_only=True)
    
    class Meta:
        model = Register
        fields = '__all__'