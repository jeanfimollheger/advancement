#je veux recuper les taches ayant la même category et project que celle qui vient d'etre "submit"

#views.py
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'your_template.html'
    success_url = reverse_lazy('task-create')  # Remplacez par votre URL de succès

    def form_valid(self, form):
        # Sauvegarder l'instance du formulaire
        self.object = form.save()

        # Récupérer les tâches avec la même catégorie et le même projet
        related_tasks = Task.objects.filter(
            category=self.object.category,
            project=self.object.project
        ).exclude(pk=self.object.pk)

        # Ajouter les tâches au contexte
        context = self.get_context_data(tasks=related_tasks)
        return self.render_to_response(context)
    
#task_form.html
<!DOCTYPE html>
<html lang="en">
  {% extends 'base.html' %}
  {% load static %}
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'css/users/style.css' %}" />
  </head>
  <body>
    {% block content %}
    <h2>Your new task ???</h2>
    <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Save</button>
    </form>
    <h2>Your other tasks about this category and project</h2>
    <ul>
      {% for task in tasks %}
      <li>
        <h3>{{ task.name }}</h3>
        h3>{{ task.target_date_task }}</h3>
      </li>
      {% endfor %}
    </ul>
    {% endblock content %}
  </body>
</html>

#####################################################################
####################################################################
#ex version au cas où
#views.py
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
  success_url= reverse_lazy('index')

  def get_context_data(self, *args, **kwargs):
    context= super().get_context_data(*args, **kwargs)
    context['tasks']=Task.objects.all()
    return context
  
  <!DOCTYPE html>
<html lang="en">
  {% extends 'base.html' %} {% load static %}
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'css/users/style.css' %}" />
  </head>
  <body>
    {% block content %}
    <h2>Your new task ???</h2>
    <form method="post">
      {% csrf_token %} {{ form.as_p }}
      <button type="submit">Save</button>
    </form>
    <h2>Your others tasks about this category && project</h2>
    <ul>
      {% for task in tasks %}
      <li>
       <h3>je veux recuper les taches ayant la même category et project que celle qui vient d'etre "submit"</h3>
      </li>
      {% endfor %}
    {% endblock content %}
  </body>
</html>
