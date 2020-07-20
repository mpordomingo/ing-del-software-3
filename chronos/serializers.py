from chronos.models import Task
from rest_framework import serializers


class TaskCreationSerializer(serializers.Serializer):
    title_defaults = {
        'required': 'Se debe especificar el titulo de la tarea. ',
        'blank': 'Se debe especificar el titulo de la tarea. '
    }
    state_defaults = {
        'required': 'Se debe especificar el estado de la tarea.',
        'blank': 'Se debe especificar el estado de la tarea.'
    }

    title = serializers.CharField(error_messages=title_defaults)
    description = serializers.CharField(required=False, allow_blank=True)
    state = serializers.CharField(error_messages=state_defaults)

    def validate_title(self, value):
        if len(value) < 2 or len(value) > 200:
            raise serializers.ValidationError("El titulo de la tarea debe contener entre 2 y 200 caracteres. ")
        return value


    def validate_state(self, value):
        if value is not None and value not in Task.valid_states():
            raise serializers.ValidationError("El estado especificado no es valido. ")
        return value

    def validate_description(self, value):
        if value is not None and len(value) > 1000:
            raise serializers.ValidationError("La descripcion no debe superar los 1000 caracteres.")
        return value

    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task


class TaskSerializer(serializers.Serializer):
    code_defaults = {
        'required': 'Se debe especificar el codigo de la tarea. ',
        'blank': 'Se debe especificar el codigo de la tarea. '
    }

    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    code = serializers.IntegerField(error_messages=code_defaults)


    def validate_title(self, value):
        if len(value) < 2 or len(value) > 200:
            raise serializers.ValidationError("El titulo de la tarea debe contener entre 2 y 200 caracteres. ")
        return value


    def validate_state(self, value):
        if value is not None and value not in Task.valid_states():
            raise serializers.ValidationError("El estado especificado no es valido. ")

        return value

    def validate_description(self, value):
        if value is not None and len(value) > 1000:
            raise serializers.ValidationError("La descripcion no debe superar los 1000 caracteres.")

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance
