from django.db import models
from main.models import PropertyType
# Create your models here.
class Features(models.Model):
    types=models.ManyToManyField("FeatureType",related_name="types")
    def __str__(self):
        return ", ".join([obj.name for obj in self.types.all()])



class FeatureType(models.Model):
    ptype=models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name
