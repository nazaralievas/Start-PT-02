from django.urls import path
from .views import *

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('movie_detail/<int:id>/', movie_detail, name='movie_detail'),
    path('rules/', rules, name='rules'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]