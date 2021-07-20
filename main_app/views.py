from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Sneaker, Accessory
from .forms import CleaningForm

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
    cleaning_form = CleaningForm()
    return render(req, 'sneakers/detail.html', {
        'sneaker': sneaker, 
        'cleaning_form': cleaning_form
    })

def add_cleaning(req, sneaker_id):
    form = CleaningForm(req.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.sneaker_id = sneaker_id
        new_cleaning.save()
    return redirect('detail', sneaker_id=sneaker_id)

class SneakerCreate(CreateView):
    model = Sneaker
    fields = '__all__'

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['model', 'colorway', 'year']

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'

def accessories_index(req):
    accessories = Accessory.objects.all()
    return render(req, 'accessories/index.html', {'accessories': accessories})

def accessories_detail(req, accessory_id):
    accessory = Accessory.objects.get(id=accessory_id)
    return render(req, 'accessories/detail.html', {'accessory': accessory})

class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'
