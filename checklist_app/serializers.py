from rest_framework import serializers
from .models import EDS, Checklist, Task

class EDSSerializer(serializers.ModelSerializer):
    class Meta:
        model = EDS
        fields = '__all__'

class ChecklistSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Checklist
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
