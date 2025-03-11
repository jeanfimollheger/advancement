from django import forms
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProjectForm, TaskForm
from .models import Category, Project, Task
from django.urls import reverse_lazy
from datetime import date, timedelta

today=date.today()
end_of_week=today+timedelta(days=6)


# Create your views here.
class ProjectListView(ListView):
  model= Project
  #queryset= Project.objects.filter(done=False)
  template_name= 'todolist/project_list.html'
  #context_object_name= 'autre_chose_que_object_list_ou_project_list'
  #form_class= ProjectForm
  
class ProjectDetailView(DetailView):
  model= Project
  template_name= 'todolist/project_detail.html'
  #context_object_name= 'autre_chose_que_object_ou_project'
  #form_class= ProjectForm

class ProjectCreateView(CreateView):
  model= Project
  template_name= 'todolist/project_form.html'
  #fields= ['name', 'target_date_project']
  form_class= ProjectForm
  success_url= reverse_lazy('todolist:projects_list')

  def get_context_data(self, *args, **kwargs):
    context= super().get_context_data(*args, **kwargs)
    context['projects']=Project.objects.all()
    return context

class ProjectUpdateView(UpdateView):
  model= Project
  template_name= 'todolist/project_form.html'
  #fields= ['name', 'target_date_project']
  form_class= ProjectForm
  
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
  #fields= ['category','project', 'name', 'target_date_task']
  form_class= TaskForm
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
  form_class= TaskForm
  
  def get_success_url(self):
    return reverse_lazy('todolist:task_list')
  
class TaskDetailView(DetailView):
  model= Task
  template_name= 'todolist/task_detail.html'
  #context_object_name= 'autre_chose_que_object_ou_task'
  form_class= TaskForm

class TaskUpdateView(UpdateView):
  model= Task
  template_name= 'todolist/task_form.html'
  #fields= ['category','project', 'name', 'target_date_task', 'done']
  form_class= TaskForm
  
  def get_success_url(self):  
    return reverse_lazy('todolist:task_detail', kwargs={'slug': self.object.slug})

class TaskDeleteView(DeleteView):
  model= Task
  template_name= 'todolist/task_confirm_delete.html'
    
  def get_success_url(self):
    return reverse_lazy('todolist:task_list') 
  
class TaskCalendarView(ListView):
  model= Task
  template_name= 'todolist/task_calendar_form.html'
  fields= ['name', 'target_date_task', 'done']

  def get_context_data(self, *args, **kwargs):
    context= super().get_context_data(*args, **kwargs)
    categories=Category.objects.all()
    context['categories']=categories
    # Créer un dictionnaire pour mapper les catégories à leurs tâches
    category_late_tasks = {category: Task.objects.filter(category=category, done= False, target_date_task__lt=today).order_by('target_date_task') for category in categories}
    print("category_late_tasks :")
    print(category_late_tasks)
    context['category_late_tasks'] = category_late_tasks
    
    category_week_tasks = {category: Task.objects.filter(category=category, done= False, target_date_task__gte=today, target_date_task__lt=end_of_week).order_by('target_date_task') for category in categories}
    print("category_week_tasks :")
    print(category_week_tasks)
    context['category_week_tasks'] = category_week_tasks

    category_future_tasks = {category: Task.objects.filter(category=category, done= False, target_date_task__gte=end_of_week).order_by('target_date_task') for category in categories}
    print("category_future_tasks :")
    print(category_future_tasks)
    context['category_future_tasks'] = category_future_tasks
    return context
  