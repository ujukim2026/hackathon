# scheduler/models.py
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in minutes


