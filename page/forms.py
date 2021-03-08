from django import forms
from . import models
from core.models import Profile
from allauth.account.forms import SignupForm


class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = models.Blog
        fields = ['title', 'body', 'author', 'images', 'thumbnail']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'images': forms.FileInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        }




class CustomSignupForm(SignupForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        # self.fields['email'].widget.attrs.update({
        #     'class': 'form-control'
        # })

        # self.fields['username'].widget.attrs.update({
        #     'class': 'form-control'
        # })

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': 'Joe'
        # })

        # self.fields['last_name'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': 'smith'
        # })

        # self.fields['password1'].widget.attrs.update({
        #     'class': 'form-control',

        # })

        # self.fields['password2'].widget.attrs.update({
        #     'class': 'form-control',

        # })

    def custom_signup(self, request, user):
        user.first_name = self.cleaned_data.pop('first_name')
        user.last_name = self.cleaned_data.pop('last_name')

        user.save()


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'image', 'cover',]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            
        }