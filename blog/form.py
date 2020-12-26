from .models import Blogs
from django.forms import ModelForm

class BlogForm(ModelForm):
    class Meta:
        model = Blogs
        fields = ['title' , 'body' , 'image']