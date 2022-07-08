from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Vinyl, Toy, Photo
from .forms import PlayingForm

import uuid
import boto3 

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'vinylcollector-avatar-9'



# Create your views here.

# def home(request):
#     '''
#     this is where we return a response
#     in most cases we  would render a template
#     and we'll need some data for that template
#     '''
#     return HttpResponse('<h1> Hello World </h1>')

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def vinyls_index(request):
  vinyls = Vinyl.objects.all()
  return render(request, 'vinyls/index.html', { 'vinyls': vinyls })

def vinyls_detail(request, vinyl_id):
  vinyl = Vinyl.objects.get(id=vinyl_id)
  playing_form = PlayingForm()
  toys_vinyl_doesnt_have = Toy.objects.exclude(id__in = vinyl.toys.all().values_list('id'))
  
  return render(request, 'vinyls/detail.html', {
    # include the cat and feeding_form in the context
    'vinyl': vinyl, 'playing_form': playing_form,
    'toys': toys_vinyl_doesnt_have
  })

def add_playing(request, vinyl_id):
  # create the ModelForm using the data in request.POST
  form = PlayingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_playing = form.save(commit=False)
    new_playing.vinyl_id = vinyl_id
    new_playing.save()
  return redirect('detail', vinyl_id=vinyl_id)


def assoc_toy(request, vinyl_id, toy_id):
  Vinyl.objects.get(id=vinyl_id).toys.add(toy_id)
  return redirect('detail', vinyl_id=vinyl_id)

def assoc_toy_delete(request, vinyl_id, toy_id):
  Vinyl.objects.get(id=vinyl_id).toys.remove(toy_id)
  return redirect('detail', vinyl_id=vinyl_id)

def add_photo(request, cat_id):
  # attempt to collect the photo file data
  photo_file = request.FILES.get('photo-file', None)
  # use conditional logic to determine if file is present
  if photo_file:
  # if it's present, we will create a reference the the boto3 client
    s3 = boto3.client('s3')
    # create a unique id for each photo file
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # funny_cat.png = jdbw7f.png
    # upload the photo file to aws s3
    try:
    # if successful
      s3.upload_fileobj(photo_file, BUCKET, key)
      # take the exchanged url and save it to the database
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # 1) create photo instance with photo model and provide cat_id as foreign key val
      photo = Photo(url=url, cat_id=cat_id)
      # 2) save the photo instance to the database
      photo.save()
    except Exception as error:
      print("Error uploading photo: ", error)
      return redirect('detail', cat_id=cat_id)
    # print an error message
  return redirect('detail', cat_id=cat_id)
  # redirect the user to the origin 

class VinylCreate(CreateView):
  model = Vinyl
  fields = ['name', 'genre', 'description', 'age']
  success_url = '/vinyls/'

class VinylUpdate(UpdateView):
  model = Vinyl
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['genre', 'description', 'age']

class VinylDelete(DeleteView):
  model = Vinyl
  success_url = '/vinyls/'

class ToyList(ListView):
  model = Toy
  template_name = 'toys/index.html'

class ToyDetail(DetailView):
  model = Toy
  template_name = 'toys/detail.html'

class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
