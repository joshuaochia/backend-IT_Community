from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Group)
admin.site.register(models.GroupPost)
admin.site.register(models.Category)
