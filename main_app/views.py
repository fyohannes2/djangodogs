from django.shortcuts import render
from .models import Vinyl

# Create your views here.

def home(request):
    '''
    this is where we return a response
    in most cases we  would render a template
    and we'll need some data for that template
    '''
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')


# Add the Vinyl class & list and view function below the imports
# class Vinyl:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.genre = genre
#     self.description = description
#     self.age = age

# vinyls = [
#   Vinyl('Lolo', 'tabby', 'foul little demon', 3),
#   Vinyl('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Vinyl('Raven', 'black tripod', '3 legged cat', 4),
#   Vinyl('In Hat', 'siamese', 'hairless', 4),
# ]

def vinyls_index(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyls/index.html', {'vinyls': vinyls})
