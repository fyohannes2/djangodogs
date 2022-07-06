from django.db import models

# Create your models here.
class Vinyl(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()
  # no need to run or re-run migrations
  def __str__(self):
    return self.name;