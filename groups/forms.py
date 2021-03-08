from django import forms
from . import models


class GroupCreateForm(forms.ModelForm):

    class Meta:
        model = models.Group
        fields = ['id', 'title', 'description', 'status', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
