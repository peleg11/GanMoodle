from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    check_police=forms.FileField()

    class Meta:
        model=User
        fields=('first_name','last_name','email',
                'check_police','password1','password2')
