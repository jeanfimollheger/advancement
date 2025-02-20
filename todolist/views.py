from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project

# Create your views here.
class ProjectListView(ListView):
  model= Project
  #queryset= Project.objects.filter(done=False)
  template_name= 'todolist/project_list.html'
  #context_object_name= 'autre_chose_que_object_list_ou_project_list'
  
class ProjectDetailView(DetailView):
  model= Project
  template_name= 'todolist/project_detail.html'
  #context_object_name= 'autre_chose_que_object_ou_project'

class ProjectCreateView(CreateView):
  model= Project
  template_name= 'todolist/project_form.html'
  fields= ['name', 'target_date_project']
  success_url= 'todolist/project_list'

  def get_context_data(self, *args, **kwargs):
    context= super().get_context_data(*args, **kwargs)
    context['projects']=Project.objects.all()
    return context
  