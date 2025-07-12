from django.urls import path
from .views import *

urlpatterns = [
    path('', movie_list, name='movie_name'),
    path('movie_detail/<int:id>/', movie_detail, name='movie_detail')
]