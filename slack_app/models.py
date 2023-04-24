from django.db import models

# Create your models here.
class City_Model(models.Model):
    city_name=models.CharField(max_length=255)
    city_pin_code=models.CharField(max_length=200)
    pass
    
class State(models.Model):
    state_name=models.CharField(max_length=255)

    pass

class Country(models.Model):
    country_name=models.CharField(max_length=200)
    country_pin_code=models.CharField(max_length=200)
    pass

# class User(models.Model):
#     pass


