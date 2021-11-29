from django.db import models
from datetime import datetime
from catalog.models import Source
from filter_wheel.models import Filter
from django.contrib.auth.models import User
# Create your models here.


class ObservationList(models.Model):
    name = models.CharField(max_length=100)

    created = models.DateTimeField(auto_created=datetime.utcnow)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    flats = models.IntegerField(default=10)
    darks = models.IntegerField(default=10)

    done = models.BooleanField(default=False)


class Observation(models.Model):
    started = models.DateTimeField()
    ended = models.DateTimeField()
    observation_list = models.ForeignKey(ObservationList, on_delete=models.CASCADE,)
    target = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    filter = models.ForeignKey(Filter, on_delete=models.SET_NULL, null=True)

    exposure_time = models.IntegerField()
