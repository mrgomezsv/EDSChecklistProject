"""
URL configuration for eds_checklist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from checklist_app.views import EDSViewSet, ChecklistViewSet, TaskViewSet, eds_list, task_list

router = routers.DefaultRouter()
router.register(r'eds', EDSViewSet)
router.register(r'checklists', ChecklistViewSet)
router.register(r'tasks', TaskViewSet)  # Agregar ruta de la API de tareas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('eds-list/', eds_list, name='eds_list'),
    path('task-list/', task_list, name='task_list'),  # Ruta para el template de tareas
]
