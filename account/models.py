from django.db import models
from django.core.validators import URLValidator


# Create your models here.
class Restaurant(models.Model):
    username      = models.CharField(max_length=30)
    name          = models.CharField(max_length=100)
    address       = models.CharField(max_length=100)
    city          = models.CharField(max_length=60)
    zipcode       = models.CharField(max_length=5)
    cuisine       = models.CharField(max_length=100)
    restaurant_id = models.CharField(max_length=10, blank=True)
    url           = models.TextField(validators=[URLValidator()], blank=True)
    user_rating   = models.FloatField(null=True, blank=True, default=None)
    num_votes     = models.IntegerField(null= True)
    average_cost_for_two = models.IntegerField(null= True)
    longitude     = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    latitude      = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    image         = models.FileField(upload_to='img/', null=True, blank=True)
    created       = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)                                    
    
