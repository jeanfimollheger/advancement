from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'target_date_project']
    widgets = {
      'target_date_project': forms.DateInput(attrs={'type': 'date'})
    }