from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()   # lectura en list/create

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'memo', 'created', 'completed']

# Serializer específico para poder actualizar "completed"
class ToDoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['completed']
