from django.db import models
from datetime import datetime
# Create your models here.


class Camera(models.Model):
    device_number = models.PositiveSmallIntegerField()


class Monitoring(models.Model):
    date = models.DateTimeField(auto_now_add=datetime.utcnow)
    temperature = models.FloatField()
    camera = models.ForeignKey(Camera, on_delete=models.SET_NULL, null=True)


class Tracker(models.Model):
    action = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=datetime.utcnow)
