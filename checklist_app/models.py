from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('TRAINER', 'Capacitador'),
        ('OPERATOR', 'Operador'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='OPERATOR')

    def __str__(self):
        return self.username



class EDS(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return self.name


class Checklist(models.Model):
    eds = models.ForeignKey(EDS, on_delete=models.CASCADE, related_name='checklists')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.eds.name}'


class Task(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='tasks')
    description = models.CharField(max_length=255)
    start_time = models.TimeField()
    duration = models.DurationField()
    is_completed = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description
