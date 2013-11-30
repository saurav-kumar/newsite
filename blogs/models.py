from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def _unicode__(self):
        return self.title

    ### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
