import django_tables2 as tables

from .models import Source, SourceType


class SourceTable(tables.Table):
    class Meta:
        model = Source
        fields = ('name', 'ra', 'dec')
        template_name = 'django_tables2/semantic.html'


class SourceTypeTable(tables.Table):
    class Meta:
        model = SourceType
        fields = ('name', 'periodic')
        template_name = 'django_tables2/semantic.html'
