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