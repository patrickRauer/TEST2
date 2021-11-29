from django.db import models

# Create your models here.


class Filter(models.Model):
    name = models.CharField(max_length=10)
    key = models.CharField(max_length=1)
    description = models.TextField(null=True)
    flat_time = models.IntegerField()
    position = models.SmallIntegerField()

    def __str__(self):
        return f'{self.name} ({self.key}/{self.position})'

