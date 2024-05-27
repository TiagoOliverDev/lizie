from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings 
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username', 'email', 'password1', 'password2']