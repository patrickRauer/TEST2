import django_tables2 as tables

from .models import Observation


class ObservationTable(tables.Table):
    class Meta:
        model = Observation
        fields = ('started', 'ended')
        template_name = 'django_tables2/semantic.html'
