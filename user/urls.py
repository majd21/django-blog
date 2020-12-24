from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signUp'),
    path('logout/' , views.logoutUser , name='logout'),
    path('login/' , views.loginUser , name='login'),
]
