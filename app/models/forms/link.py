from django import forms
from app.models.link import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['link', 'description']
        extra_kwargs = {
            'link': {'required': True},
            'description': {'required': False},
        }
