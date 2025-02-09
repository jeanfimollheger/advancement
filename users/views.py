from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import UserSignUpForm, UserLoginForm

# Create your views here.
def index(request):
  return render(request, 'base.html')



class UserSignUpView(CreateView):
  model = User
  form_class = UserSignUpForm
  template_name = 'users/signup.html'
  success_url = reverse_lazy('login')

  def form_valid(self, form):
      print("Le formulaire est valide")  # Vérification
      return super().form_valid(form)

  def form_invalid(self, form):
      print("Le formulaire est invalide :", form.errors)  # Vérification
      return super().form_invalid(form)



class UserLoginView(LoginView):
  authentication_form = UserLoginForm
  template_name = 'users/login.html'
  success_url = reverse_lazy('index') 



class UserLogoutView(LogoutView):
  next_page = reverse_lazy('index') 
    
    
