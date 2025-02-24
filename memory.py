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
        <!-- Ajoutez d'autres détails de la tâche si nécessaire -->
      </li>
      {% endfor %}
    </ul>
    {% endblock content %}
  </body>
</html>