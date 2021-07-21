from django.contrib import admin

# Register your models here.
from .models import Sneaker, Cleaning, Accessory

admin.site.register(Sneaker)
admin.site.register(Cleaning)
admin.site.register(Accessory)