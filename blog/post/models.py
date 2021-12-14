import os
import uuid

from django.db import models

# Create your models here.


class Post(models.Model):

    slug = models.CharField(verbose_name="Post Slug", max_length=120)
    title = models.CharField(verbose_name="Post Title", max_length=100)
    content = models.TextField(verbose_name="Post Content")

    views = models.PositiveIntegerField(
        verbose_name="Post Views", default=0, editable=False
    )
    created_on = models.DateTimeField(
        verbose_name="Post Created Date", auto_now_add=True
    )
    modified_on = models.DateTimeField(verbose_name="Post Modified Date", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post"


class Image(models.Model):
    origin_filename = models.CharField(
        verbose_name="Original Image Name", max_length=80
    )

    def _get_uuid_path(instance, filename):
        uuid4 = uuid.uuid4()

        new_path = os.path.join("upload/", f"{uuid4}_{filename}")
        return new_path

    path = models.ImageField(verbose_name="Image Path", upload_to=_get_uuid_path)

    def __str__(self):
        return self.path

    class Meta:
        db_table = "image"
