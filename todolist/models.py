from django.db import models
from django.utils import timezone

class todoItem(models.Model):
    class priority(models.IntegerChoices):
        HIGH = 3
        MEDIUM = 2
        LOW = 1

    description = models.TextField(blank='false')
    created_at = models.DateTimeField(default=timezone.now())
    priority = models.IntegerField(choices=priority.choices, default=1)

    def __str__(self):
        return description
    
