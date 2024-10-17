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
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación
from rest_framework import routers

from checklist_app import views
from checklist_app.views import EDSViewSet, ChecklistViewSet, TaskViewSet, eds_list, task_list, dashboard, register

# Definir el router y registrar las vistas de las API
router = routers.DefaultRouter()
router.register(r'eds', EDSViewSet)
router.register(r'checklists', ChecklistViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('api/', include(router.urls)),  # Incluir las rutas del router de API
    path('eds-list/', eds_list, name='eds_list'),
    path('task-list/', task_list, name='task_list'),
]
