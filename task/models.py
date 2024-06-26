from django.db import models
from django.contrib.auth.models import User
import datetime

class Task(models.Model):
    TASK_PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=5)
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    due_date = models.DateField(default=datetime.date.today)
    priority = models.CharField(max_length=6, choices=TASK_PRIORITY_CHOICES, default='Medium')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Adjust this to return a meaningful representation

    class Meta:
        ordering = ['-created_at']  # Orders tasks by created_at descending by default
