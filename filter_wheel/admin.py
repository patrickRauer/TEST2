from django.contrib import admin

# Register your models here.
from .models import Filter


@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ['name', 'key', 'position', 'flat_time']