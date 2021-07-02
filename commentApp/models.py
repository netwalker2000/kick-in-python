# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


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
        app_label = "commentApp"

