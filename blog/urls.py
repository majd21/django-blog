from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('profile/', views.profile, name='profile'),
    path('profile/create', views.createblog, name='createblog'),
    path('profile/delete/<int:blog_pk>', views.deleteblog, name='deleteblog'),
    path('profile/edit/<int:blog_pk>', views.editblog, name='editblog'),
    path('blogs/<int:blog_pk>', views.viewblog, name='viewblog')
]
