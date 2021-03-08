from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()

group_status = [
    ('Public', 'Public'),
    ('Private', 'Private'),
    ('Close', 'Close'),
]


class Group(models.Model):
    title = models.CharField(max_length=99)
    admin = models.ManyToManyField(User, related_name='admin')
    data_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=656)
    members = models.ManyToManyField(User, related_name='members')
    cover = models.ImageField(blank=True, upload_to='group_cover/')
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=50, choices=group_status)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:group_detail", kwargs={'slug': self.slug})

category_choices = [
    ('Django', 'Django'),
    ('React', 'React'),
    ('Laravel', 'Lavarel'),
    ('Angular', 'Angular'),
]

class Category(models.Model):
    name = models.CharField(max_length=56, choices=category_choices, default='Django')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class GroupPost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='group_posts'
        )

    groups = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='post'
        )
    body = RichTextUploadingField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    @staticmethod
    def get_all_post(self):

        return GroupPost.objects.all()

    @staticmethod
    def get_all_post(self):

        return GroupPost.objects.filter(category=self.category)


    def get_absolute_url(self):
        return reverse(
            "groups:group_detail",
            kwargs={'slug': self.groups.slug}
            )
