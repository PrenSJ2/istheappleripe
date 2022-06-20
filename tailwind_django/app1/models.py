from django.db import models
from django.contrib import admin

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    status_info = models.CharField(max_length=100)
    img = models.URLField()
    daysSince = models.CharField(max_length=100)
    avg = models.CharField(max_length=100)
    color = models.CharField(max_length=100)


    def __str__(self):
        return "name:" + self.name + " status: " + self.status + " status_info: " + self.status_info + " img: " + self.img + " daysSince: " + self.daysSince + " avg: " + self.avg + " color: " + self.color

