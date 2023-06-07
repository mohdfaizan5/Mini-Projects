from django.db import models

# Create your models here.
class Url(models.Model):

  # What properties it should have
  url = models.CharField(max_length=2000)
  uuid = models.CharField(max_length=10)

  # methods
  def __str__(self):
      return self.url
  