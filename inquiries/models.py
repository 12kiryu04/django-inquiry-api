from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Inquiry(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('CLOSED', 'Closed'),
        ]
    
    PRIORITY_CHOICES = [
        ('LOW','Low'),
        ('MEDIUM','Medium'),
        ('HIGH','High'),
        ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content =models.TextField()
    status =  models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title