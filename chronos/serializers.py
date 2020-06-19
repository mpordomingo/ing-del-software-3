from chronos.models import Task
from rest_framework import serializers

class TaskSerializer(serializers.Serializer):

    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()