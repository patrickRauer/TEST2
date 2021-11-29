from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    content = {'section': 'main',
               'title': 'Index'}
    return render(request, 'main/index.html', context=content)
