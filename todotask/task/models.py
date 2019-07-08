from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=120)
    creation_date = models.DateTimeField(default=timezone.now())
    modification_time = models.DateTimeField(default=timezone.now())
    completed_time = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
