from django.db import models
from django.shortcuts import get_object_or_404
from django.http import FileResponse
# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    file = models.FileField(upload_to='static/documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    