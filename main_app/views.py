from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Sneaker

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def sneakers_index(req):
    sneakers = Sneaker.objects.all()
    return render(req, 'sneakers/index.html', {'sneakers': sneakers})

def sneakers_detail(req, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    return render(req, 'sneakers/detail.html', {'sneaker': sneaker})

class SneakerCreate(CreateView):
    model = Sneaker
    fields = '__all__'

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['model', 'colorway', 'year']

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'