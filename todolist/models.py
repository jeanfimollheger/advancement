from datetime import date, timedelta
from django.db import models
from django.utils.text import slugify

def default_target_date():
  return date.today() + timedelta(days=1)


# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, blank=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return f'{self.name} ({self.pk})'
  


class Project(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, blank=True)
  target_date_project = models.DateField(default=default_target_date)
  historic_target_date_project= models.JSONField(default=list, blank=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    if self.pk is None:
      self.historic_target_date_project.append(self.target_date_project)
    else :  
      original= Project.objects.get(pk=self.pk)
      if original.target_date_project != self.target_date_project:
        self.historic_target_date_project.append(self.target_date_project)
    super().save(*args, **kwargs)

  def __str__(self):
    return f'{self.name} ({self.pk})'
  


class Task(models.Model):
  category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
  project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projects", null=True, blank=True)
  name=models.CharField(max_length=220, unique=True)
  slug=models.SlugField(max_length=220, unique=True, blank=True)
  target_date_task = models.DateField(default=default_target_date)
  done= models.BooleanField(default=False)
  creation_date=models.DateField(default=date.today)
  historic_target_date_task = models.JSONField(default=list, blank=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    if self.pk is None:
      self.historic_target_date_task.append(self.target_date_task)
    else :  
      original= Task.objects.get(pk=self.pk)
      if original.target_date_task != self.target_date_task:
        self.historic_target_date_task.append(self.target_date_task)
    super().save(*args, **kwargs)

  def __str__(self):
    return f'{self.name} [{self.category}/{self.project}] ({self.pk})'  