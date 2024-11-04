from django.db import models

# Create your models here.

class Room(models.Model):
    
    name = models.CharField(max_length=100)
    # roomCreator = models.ForeignKey("user")
    
class Message(models.Model):
    
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    
