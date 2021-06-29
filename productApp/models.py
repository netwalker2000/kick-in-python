from django.db import models

# Create your models here.
class Product :
    id = models.IntegerField
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    status = models.IntegerField
    created_at = models.TimeField
    updated_at = models.TimeField