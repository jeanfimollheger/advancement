from django import forms
from  .models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'password1', 'password2'] 