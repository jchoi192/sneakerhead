from django.contrib import admin

# Register your models here.
from .models import Sneaker
from .models import Cleaning

admin.site.register(Sneaker)
admin.site.register(Cleaning)