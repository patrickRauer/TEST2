from django.db import models
from django.contrib.auth.models import User
from catalog.models import Source
from filter_wheel.models import Filter
# Create your models here.


class ImageTye(models.Model):
    name = models.CharField(max_length=100)


class Image(models.Model):
    target = models.ForeignKey(Source, models.SET_NULL, null=True)
    filter = models.ForeignKey(Filter, models.SET_NULL, null=True)
    type = models.ForeignKey(ImageTye, on_delete=models.SET_NULL, null=True)

    exposure_time = models.FloatField()
    exposure_started = models.DateTimeField()

    observer = models.ForeignKey(User, models.SET_NULL, null=True)

    fits_file = models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        target_name = self.target.name if self.target else ''
        return f'{target_name} (started at {self.exposure_started} with exposure time of {self.exposure_time})'
