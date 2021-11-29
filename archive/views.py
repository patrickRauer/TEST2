from django.shortcuts import render
from django_tables2 import SingleTableView
from .tables import ImageTable
from .models import Image
# Create your views here.

from django.http import HttpResponse


class ImageTableView(SingleTableView):
    table_class = ImageTable
    template_name = 'archive/index.html'
    model = Image
