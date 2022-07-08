from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# A tuple of 2-tuples
PLAYS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return f'{self.color} {self.name}'

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})
    
class Vinyl(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def played_for_today(self):
    return self.playing_set.filter(date=date.today()).count() >= len(PLAYS)
  # no need to run or re-run migrations
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'vinyl_id': self.id})

class Playing(models.Model):
  date = models.DateField('playing date')
  play = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=PLAYS,
    # set the default value for play to be 'B'
    default=PLAYS[0][0]
  )
  # CREATE A VINYL_ID FK
  vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

  def __str__(self):    
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_play_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']

class Photos(models.Model):
  url = models.CharField(max_length=200)
  vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for vinyl_id: {self.vinyl.id} @{self.url}"
