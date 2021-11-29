from django.urls import path

from . import views

app_name = 'filter_wheel'
urlpatterns = [
    path('', views.FilterTableView.as_view(), name='index'),
    path('add/', views.FilterFormView.as_view(), name='add')
]
