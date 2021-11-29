from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django_tables2 import SingleTableView

from .forms import FilterForm
from .tables import FilterTable, Filter
# Create your views here.


class FilterFormView(FormView):
    form_class = FilterForm
    template_name = 'camera/form.html'
    success_url = reverse_lazy('camera:update')


class FilterTableView(SingleTableView):
    table_class = FilterTable
    template_name = 'filter_wheel/table.html'
    model = Filter
