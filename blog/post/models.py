import os
import uuid

from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=120, unique=True)
    content = models.CharField(max_length=3000)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "post"


class Image(models.Model):
    origin_filename = models.CharField(max_length=80)

    def _get_uuid_path(instance, filename):
        uuid4 = uuid.uuid4()

        new_path = os.path.join("upload/", f"{uuid4}_{filename}")
        return new_path

    path = models.ImageField(upload_to=_get_uuid_path)

    class Meta:
        db_table = "image"
