from django.db import models
from datetime import datetime


# Create your models here.

class Blog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.date}"

