from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Task
from django.urls import reverse_lazy

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
  success_url= reverse_lazy('todolist:projects_list')

  def get_context_data(self, *args, **kwargs):
    context= super().get_context_data(*args, **kwargs)
    context['projects']=Project.objects.all()
    return context

class ProjectUpdateView(UpdateView):
  model= Project
  template_name= 'todolist/project_form.html'
  fields= ['name', 'target_date_project']
  
  def get_success_url(self):
    return reverse_lazy('todolist:project_detail', kwargs={'pk': self.object.pk})
  
class ProjectDeleteView(DeleteView):
  model= Project
  template_name= 'todolist/project_confirm_delete.html'
  #success_url= reverse_lazy('todolist:projects_list')
  
  def get_success_url(self):
    return reverse_lazy('todolist:projects_list')
  
class TaskCreateView(CreateView):
  model= Task
  template_name= 'todolist/task_form.html'
  fields= ['category','project', 'name', 'target_date_task']
  success_url= reverse_lazy('todolist:task-create')

  def get_context_data(self, *args, **kwargs):
    context= super().get_context_data(*args, **kwargs)
    context['tasks']=Task.objects.all()
    return context
    
  def form_valid(self, form):
    # Sauvegarder l'instance du formulaire
    self.object = form.save()
    context= super().get_context_data()
    context['related_tasks']=Task.objects.filter(category=self.object.category, project=self.object.project).exclude(pk=self.object.pk)
    return self.render_to_response(context)

class TaskListView(ListView):
  model= Task
  template_name= 'todolist/task_list.html'
  #context_object_name= 'autre_chose_que_object_list_ou_task_list'
  
  def get_success_url(self):
    return reverse_lazy('todolist:task_list')
  
class TaskDetailView(DetailView):
  model= Task
  template_name= 'todolist/task_detail.html'
  #context_object_name= 'autre_chose_que_object_ou_task'