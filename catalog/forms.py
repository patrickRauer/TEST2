from django import forms

from .models import Source, SourceType


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = '__all__'


class SourceTypeForm(forms.ModelForm):
    class Meta:
        model = SourceType
        fields = '__all__'
