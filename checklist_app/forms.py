# checklist_app/forms.py

from django import forms
from checklist_app.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User  # Asegúrate de usar tu modelo de usuario personalizado
        fields = ('username', 'email')  # Los campos que quieras incluir en el formulario
