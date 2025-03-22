from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'target_date_project']
    widget= {'target_date_project': forms.DateInput(attrs={'type':'date'})
             }
    
class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['category','name', 'target_date_task', 'done']
    widget= {'target_date_task': forms.DateInput(attrs={'type':'date'}),
             'done': forms.CheckboxInput(),
            }