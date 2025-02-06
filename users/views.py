from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import UserSignUpForm

# Create your views here.
def index(request):
  return render(request, 'base.html')

class UserSignUpView(CreateView) :
  model = User
  form_class = UserSignUpForm
  template_name = 'users/signup.html'
  success_url = reverse_lazy('login')
