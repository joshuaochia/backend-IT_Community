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


class GroupPostForm(forms.ModelForm):

    class Meta:
        model = models.GroupPost
        fields = ['body', 'categories']

        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'})

        }
