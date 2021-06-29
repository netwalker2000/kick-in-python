from django.db import models


# Create your models here.
class ProductTab(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    status = models.IntegerField()


    class Meta:
        db_table = "product_tab"
