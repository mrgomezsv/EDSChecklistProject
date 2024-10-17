from django.shortcuts import render
from rest_framework import viewsets
from .models import EDS, Checklist, Task
from .serializers import EDSSerializer, ChecklistSerializer, TaskSerializer

# API Views
class EDSViewSet(viewsets.ModelViewSet):
    queryset = EDS.objects.all()
    serializer_class = EDSSerializer

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# HTML Views
def eds_list(request):
    return render(request, 'eds_list.html')

def task_list(request):
    return render(request, 'task_list.html')

# Vista para el dashboard (si es que la necesitas)
def dashboard(request):
    return render(request, 'dashboard.html')
