from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
# Create your views here.
from .forms import ObservationForm, ObservationCatalogForm
from .boards.visibility_chart.main import app as visibility_app
from .tables import ObservationTable, Observation


class ObservationFormView(FormView):
    form_class = ObservationForm
    template_name = 'observation/form.html'
    success_url = reverse_lazy('observation:index')


class ObservationCatalogFormView(FormView):
    form_class = ObservationCatalogForm
    template_name = 'observation/form_catalog.html'
    success_url = reverse_lazy('observation:index')


class ObservationTableView(SingleTableView):
    table_class = ObservationTable
    template_name = 'observation/index.html'
    model = Observation
