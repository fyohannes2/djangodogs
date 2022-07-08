from django.contrib import admin
# import your models here
from .models import Vinyl, Playing, Toy, Photo 

# make sure to register the model
admin.site.register(Vinyl)

admin.site.register(Playing)

admin.site.register(Toy)

admin.site.register(Photo)