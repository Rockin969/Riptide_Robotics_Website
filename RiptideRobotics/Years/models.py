from django.db import models

# Create your models here.

class Years(models.Model):
    season = models.CharField(max_length=64, null=True)
    competion = models.TextField(null=True)
    officialinfo = models.TextField(null=True)
    build = models.TextField(null=True)
    video1 = models.TextField(null=True)
    caption1 = models.TextField(null=True)
    image1 = models.FileField(upload_to='static/img/', null=True, verbose_name="")
    caption2 = models.TextField(null=True)
    competition = models.TextField(null=True)
    video2 = models.TextField(null=True)
    caption3 = models.TextField(null=True)
    image2 = models.FileField(upload_to='static/img/', null=True, verbose_name="")
    caption4 = models.TextField(null=True)
    conclusion = models.TextField(null=True)

def __str__(self):
        return f"{self.id}: {self.season}"