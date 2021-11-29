from django.shortcuts import render
from django.views.generic import FormView
from django_tables2 import SingleTableView
# Create your views here.
from .models import Source, SourceType
from .forms import SourceTypeForm, SourceForm
from .tables import SourceTable, SourceTypeTable

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class SourceTableView(SingleTableView):
    template_name = 'catalog/index.html'
    table_class = SourceTable
    model = Source


class SourceTypeTableView(SingleTableView):
    template_name = 'catalog/index.html'
    table_class = SourceTypeTable
    model = SourceType


class SourceFormView(FormView):
    form_class = SourceForm
    template_name = 'catalog/form.html'


class SourceTypeFormView(FormView):
    form_class = SourceTypeForm
    template_name = 'catalog/form.html'
