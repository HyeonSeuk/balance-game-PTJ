from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    selected_option = models.CharField(max_length=200, blank=True)
    select1_contents = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='selected_option1_posts', blank=True)
    select2_contents = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='selected_option2_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
