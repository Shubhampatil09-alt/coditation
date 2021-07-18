from django.db import models
from django.db.models.base import Model

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    category = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name 
# Create your models here.
