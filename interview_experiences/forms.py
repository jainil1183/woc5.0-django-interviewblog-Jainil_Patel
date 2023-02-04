from django import forms
from django.forms import ModelForm
from .models import experience

class experienceForm(ModelForm):
    class Meta:
        model = experience
        fields = ('title','author','company', 'type_offer', 'job_profile', 'year', 'content')
        labels = {
            'title': '',
            'author': '',
            'company': '',
            'type_offer': '',
            'job_profile': '',
            'year': '',
            'content': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Unique Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'type_offer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type of Offer'}),
            'job_profile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Profile'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Content'}),
        }