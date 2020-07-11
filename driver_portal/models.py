from django.db import models

# Create your models here.


class driver(models.Model):
    bus_number = models.CharField(max_length=100)
    driver_first_name  = models.CharField(max_length=100)
    driver_last_name = models.CharField(max_length=100)
    driver_username = models.CharField(max_length=100)
    driver_password = models.CharField(max_length=100)
    driver_email = models.CharField(max_length=100)