from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=False, upload_to='blogs/images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blogs , on_delete=models.CASCADE , related_name='comments')

class Posts(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='posts/images/')
    url = models.URLField()

    def __str__(self):
        return self.title
