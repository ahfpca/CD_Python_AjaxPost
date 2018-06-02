from __future__ import unicode_literals
from django.db import models


class PostManager(models.Manager):
    def record_validator(self, postData):
        errors = {}
        if len(postData["note"].strip()) < 10:
            errors["name"] = "Note should be at least 10 characters"

        return errors


# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = PostManager()
