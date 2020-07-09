from django.db import models

# Create your models here.

class details(models.Model):
    bus_number = models.CharField(max_length=100)
    origin_place = models.CharField(max_length=100)
    destination_place = models.CharField(max_length=100)
    bus_type = models.CharField(max_length=100)
    journey_date = models.DateField()
    depature_time = models.CharField(max_length=100)