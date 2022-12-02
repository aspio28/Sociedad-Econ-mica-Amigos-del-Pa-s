from django.db import models
from django.urls import reverse

class Document(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("document.html", args=[str(self.id)])
    
