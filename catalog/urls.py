from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.SourceTableView.as_view(), name='index'),
    path('add/', views.SourceFormView.as_view(), name='add'),
    path('source_types/', views.SourceTypeTableView.as_view(), name='source_types'),
    path('source_types/add/', views.SourceTypeFormView.as_view(), name='source_types_add'),
]
