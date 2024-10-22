from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .forms import CustomUserCreationForm
from .models import EDS, Checklist, Task
from .serializers import EDSSerializer, ChecklistSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Vistas API
class EDSViewSet(viewsets.ModelViewSet):
    queryset = EDS.objects.all()
    serializer_class = EDSSerializer
    permission_classes = [IsAuthenticated]  # Solo permite a usuarios autenticados interactuar

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@login_required
def eds_list(request):
    estaciones = EDS.objects.all()  # Obtén todas las estaciones del modelo EDS
    return render(request, 'eds_list.html', {'estaciones': estaciones})

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
