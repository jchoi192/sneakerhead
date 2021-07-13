from django.db import models

# Create your models here.
class Sneakerhead(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    year = models.IntegerField()