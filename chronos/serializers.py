from chronos.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    state = serializers.CharField(max_length=200)


    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task