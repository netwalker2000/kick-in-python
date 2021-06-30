from django.db import models


# Create your models here.
class ProductTab(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    status = models.IntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        db_table = "product_tab"


class PhotoTab(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    url = models.CharField(max_length=2000)
    product_id = models.IntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        db_table = "photo_tab"


class CommentTab(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=2000)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=200)
    status = models.IntegerField()
    topic_id = models.IntegerField()
    to_id = models.IntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        db_table = "comment_tab"

