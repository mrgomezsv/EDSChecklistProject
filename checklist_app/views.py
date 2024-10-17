from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import EDS, Checklist, Task
from .serializers import EDSSerializer, ChecklistSerializer, TaskSerializer
from django.shortcuts import render, redirect
from checklist_app.forms import CustomUserCreationForm  # Importar el formulario personalizado
from django.contrib.auth import login
from django.contrib import messages

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


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # Verificar si el formulario es válido
            user = form.save()  # Guardar el nuevo usuario
            login(request, user)  # Iniciar sesión automáticamente
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('dashboard')  # Redirigir al dashboard
        else:
            print(form.errors)  # Imprimir errores del formulario en la consola para depuración
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})