from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        default=None)
    
    def time_passed(self):
        today = datetime.now().date()
        delta = today - self.created_at.date()

        return delta.days