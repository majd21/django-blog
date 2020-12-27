from .models import Blogs ,Comments
from django.forms import ModelForm

class BlogForm(ModelForm):
    class Meta:
        model = Blogs
        fields = ['title' , 'body' , 'image']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name' , 'body']