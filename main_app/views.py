from django.shortcuts import render

# temporary sneaker class
class Sneaker():
    def __init__(self, brand, model, colorway, year):
        self.brand = brand
        self.model = model
        self.colorway = colorway
        self.year = year

sneakers = [
    Sneaker('Jordan', '1', 'Bred', 1995),
    Sneaker('Adidas', 'Yeezy Boost 350', 'Carbon', 2018),
    Sneaker('Nike', 'Undefeated x Zoom Kobe 5 Protro', 'Hall of Fame', 2021),
    Sneaker('Nike', 'Air Presto Off-White', 'White', 2018),
    Sneaker('New Balance', '2002R Salehe Bembury ', 'Water Be The Guide', 2021),
]


# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def sneakers_index(req):
    return render(req, 'sneakers/index.html', {'sneakers': sneakers})