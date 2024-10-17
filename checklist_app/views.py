from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import EDS, Checklist, Task
from .serializers import EDSSerializer, ChecklistSerializer, TaskSerializer

# Vista para el dashboard (requiere login)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Vistas API
class EDSViewSet(viewsets.ModelViewSet):
    queryset = EDS.objects.all()
    serializer_class = EDSSerializer

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Vistas HTML para listas
def eds_list(request):
    return render(request, 'eds_list.html')

def task_list(request):
    return render(request, 'task_list.html')
