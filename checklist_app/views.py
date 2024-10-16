from rest_framework import viewsets
from django.shortcuts import render
from .models import EDS, Checklist, Task
from .serializers import EDSSerializer, ChecklistSerializer, TaskSerializer

class EDSViewSet(viewsets.ModelViewSet):
    queryset = EDS.objects.all()
    serializer_class = EDSSerializer

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def eds_list(request):
    return render(request, 'eds_list.html')
