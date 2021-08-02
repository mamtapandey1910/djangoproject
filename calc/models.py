from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class MyModel(models.Model):
    id = models.AutoField()
    full_name = models.CharField(max_length= 200)
    mob_no = models.IntegerField(max_length=15)