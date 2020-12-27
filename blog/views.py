from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs, Comments, Posts
from .form import BlogForm, CommentForm

# Create your views here.


def home(request):
    posts = Posts.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def profile(request):
    userblogs = Blogs.objects.filter(user=request.user)
    return render(request, 'blog/profile.html', {'userblogs': userblogs, 'form': BlogForm()})


def createblog(request):
    if request.method == 'GET':
        return render(request, 'blog/createblog.html', {'form': BlogForm()})
    else:
        try:
            form = BlogForm(request.POST)
            newBlog = form.save(commit=False)
            newBlog.user = request.user
            newBlog.save()
            return redirect('profile')
        except ValueError:
            return render(request, 'blog/createblog.html', {'form': BlogForm(), 'error': 'Bad Data pass in!'})


def deleteblog(request, blog_pk):
    blog = get_object_or_404(Blogs, pk=blog_pk, user=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('profile')


def editblog(request, blog_pk):
    blog = get_object_or_404(Blogs, pk=blog_pk, user=request.user)
    if request.method == 'POST':
        try:
            form = BlogForm(request.POST, instance=blog)
            form.save()
            return redirect('profile')
        except ValueError:
            return render(request, 'blog/profile.html', {'form': BlogForm(), 'error': 'Bad Data pass in!'})


def viewblog(request, blog_pk):
    blog = get_object_or_404(Blogs, pk=blog_pk)
    if request.method == 'GET':
        return render(request, 'blog/viewblog.html', {'blog': blog, 'form': CommentForm()})
    else:
        form = CommentForm(request.POST)
        newComment = form.save(commit=False)
        newComment.blog = blog
        newComment.save()
        return redirect('viewblog', blog_pk=blog.pk)
