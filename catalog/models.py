from django.db import models

# Create your models here.


class SourceType(models.Model):
    name = models.CharField(max_length=100)
    periodic = models.BooleanField()


class Source(models.Model):
    name = models.CharField(max_length=100)
    ra = models.FloatField()
    dec = models.FloatField()

    type = models.ForeignKey(SourceType, models.SET_NULL, null=True)

    def __str__(self):
        return self.name
