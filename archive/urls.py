from django.urls import path

from . import views

app_name = 'archive'

urlpatterns = [
    path('', views.ImageTableView.as_view(), name='index'),
]
