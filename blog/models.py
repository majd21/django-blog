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
