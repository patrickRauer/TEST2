from django import forms
from filter_wheel.models import Filter
from catalog.models import Source


class ObservationForm(forms.Form):
    name = forms.CharField(max_length=100)
    filter = forms.ModelChoiceField(queryset=Filter.objects.all())

    exposure_time = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 0, 'max': 600, 'steps': 1}))


class ObservationCatalogForm(forms.Form):
    target = forms.ModelChoiceField(queryset=Source.objects.all())
    filter = forms.ModelChoiceField(queryset=Filter.objects.all())

    exposure_time = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 0, 'max': 600, 'steps': 1}))
