from django.db import models
from django.urls import reverse

# Create your models here.
class Sneaker(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.brand} {self.model} {self.colorway} {self.year}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sneaker_id': self.id})

class Cleaning(models.Model):
    AREAS = (
        ('IS', 'Inner Sole'),
        ('MS', 'Mid Sole'),
        ('OS', 'Outer Sole'),
        ('L', 'Laces'),
        ('T', 'Tongue')
    )

    date = models.DateField('Cleaned on: ')
    area = models.CharField(
        max_length=2, 
        choices=AREAS, 
        default=AREAS[0][0]
    )

    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_area_display()} on {self.date}'

    class Meta:
        ordering = ['-date']

class Accessory(models.Model):
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name