from dataclasses import fields
from django.forms import ModelForm
from .models import Take
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(ModelForm):
    class Meta:
        model=Take
        fields='__all__'
        exclude=['roll','cname','contact','mob']

class SignUpForm(UserCreationForm):
    name=forms.CharField(max_length=100, required=False, help_text='Optional.')
    mob=forms.IntegerField(required=False)
    cname=forms.CharField(max_length=100, required=False, help_text='Optional.')

    
    class Meta:
        model = User
        fields = ('username', 'name', 'password1', 'password2', 'mob','cname',)
        labels = {'mob': 'Mobile Number','username': 'e-Mail ID'}