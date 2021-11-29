from django.contrib import admin
from .models import Source
# Register your models here.


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'ra', 'dec']
