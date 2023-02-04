from django import forms

from django.forms import ModelForm

from .models import customer
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password,check_password


class ProfileForm(forms.ModelForm):
    extra_field = forms.ImageField()

    class Meta:
        model = User
        fields = ['degree', 'program', 'graduation_year']
'''
class customerForm(ModelForm):
    class Meta:
        model = customer
        fields = "__all__"

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'degree': 'Degree',
            'program': 'Program',
            'password': '',
            'graduation_year': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'abc@xyz.com'}),
            'degree': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Degree'}),
            'program': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Program'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Graduation Year'}),
        }
'''