from django.db import models

# Create your models here.
class Guitar(models.Model):
    brand=models.CharField(max_length=100)
    guitarname=models.CharField(max_length=100)
    finish=models.CharField(max_length=100)
    year=models.IntegerField()
    origin=models.CharField(max_length=100)
    finish=models.CharField(max_length=100)
    fretboardtype=models.CharField(max_length=100)
    bodymaterial=models.CharField(max_length=100)
    pickups=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    condition=models.CharField(max_length=100)
    seller=models.CharField(max_length=100)
    img=models.CharField(max_length=200)
    