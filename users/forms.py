from django import forms
from  .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserSignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'password1', 'password2'] 

  def save(self, commit=True):
    print("Méthode save() appelée")  # Vérification
    user = super().save(commit=False)
    user.is_active = True
    print("Utilisateur enregistré :", user.username)  # Vérification
    if commit:
        user.save()
        print("Utilisateur sauvegardé en base")  # Vérification
    return user

class UserLoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'})) 