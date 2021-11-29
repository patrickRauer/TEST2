import django_tables2 as tables

from . import models


class ImageTable(tables.Table):
    class Meta:
        model = models.Image
        fields = ('target', 'filter', 'type', 'exposure_started', 'exposure_time', 'user')
        template_name = 'django_tables2/semantic.html'
