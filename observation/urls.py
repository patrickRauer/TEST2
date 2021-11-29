from django.urls import path

from . import views

app_name = 'observation'

urlpatterns = [
    path('', views.ObservationTableView.as_view(), name='index'),
    path('standard/', views.ObservationFormView.as_view(), name='standard'),
    path('catalog/', views.ObservationCatalogFormView.as_view(), name='catalog')
]
