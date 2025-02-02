from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.
class User (AbstractUser):
  slug = models.SlugField(blank= True)

  def save(self, *args, **kwargs):
    if not self.slug :
      self.slug = slugify(self.username)
    super().save(*args, **kwargs)