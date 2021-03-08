from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=256, unique=True)
    body = RichTextUploadingField(blank=True, null=True)
    author = models.CharField(max_length=56, null=True)
    images = models.ImageField(upload_to='blog/cover/', blank=True, null=True)
    thumbnail = models.ImageField(
        default='blog/thumbnail/default.png',
        blank=True, upload_to='blog/thumbnail'
        )
    slug = models.SlugField()
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("page:blog_detail", kwargs={"slug": self.slug})
