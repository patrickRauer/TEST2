"""TEST_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.urls import api

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('archive/', include('archive.urls')),
    path('catalog/', include('catalog.urls')),
    path('main/', include('main.urls')),
    path('camera/', include('camera.urls')),
    path('filter_wheel/', include('filter_wheel.urls')),
    path('observation/', include('observation.urls')),
    path('settings/', include('settings.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('api/', api.urls)
]