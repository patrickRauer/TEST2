import django_tables2 as tables

from .models import Filter


class FilterTable(tables.Table):

    class Meta:
        model = Filter
        fields = ('name', 'key', 'position', 'flat_time')
        template_name = 'django_tables2/semantic.html'
