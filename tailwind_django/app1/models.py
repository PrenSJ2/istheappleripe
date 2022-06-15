from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    status_info = models.CharField(max_length=100)
    img = models.URLField()
    daysSince = models.IntegerField()
    avg = models.IntegerField()

    def __str__(self):
        return "name:" + self.name + " status: " + self.status + " status_info: " + self.status_info + " img: " + self.img + " daysSince: " + self.daysSince + " avg: " + self.avg