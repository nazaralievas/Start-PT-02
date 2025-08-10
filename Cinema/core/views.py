from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .models import Movie, Comment
from .forms import CommentForm



def movie_list(request):
    q = request.GET.get('q')
    if q:
        movies = Movie.objects.filter(name_lower__icontains=q.lower())
    else:
        movies = Movie.objects.all()
    return render(request, 'core/movie_list.html', {'movies': movies})


def movie_detail(request, id):
    form = CommentForm()
    movie = Movie.objects.get(id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
            return redirect('movie_detail', id=movie.id)
    return render(request, 'core/movie_detail.html', {'movie': movie, 'form': form})


def rules(request):
    return render(request, 'core/rules.html')


# ------ login, registration, logout ---------
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth

def login(request):
    if request.user.is_authenticated:
        return redirect('movie_list')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth.login(request, user)
                return redirect('movie_list')
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('movie_list')


def register(request):
    if request.user.is_authenticated:
        return redirect('movie_list')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})


def edit_comment(request, id):
    comment = Comment.objects.get(id=id)
    
    if comment.user != request.user:
        return HttpResponseForbidden('Вы не можете редактировать этот комментарий!')

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', id=comment.movie.id)

    form = CommentForm(instance=comment)
    return render(request, 'core/edit_comment.html',
                  {'comment': comment, 'form': form})


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if comment.user != request.user:
        return HttpResponseForbidden('Вы не можете удалить этот комментарий!')

    if request.method == 'POST':
        comment.delete()
        return redirect('movie_detail', id=comment.movie.id)

    return render(request, 'core/delete_comment.html', {'comment': comment})

# pip install requests
import requests
def random_dog(request):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    dog_image_url = response.json().get("message")
    return render(request, 'core/random_dog.html', {'dog_image_url': dog_image_url})


from django.contrib.auth.models import User

def user_profile(request, id):
    profile_user = User.objects.get(id=id)
    return render(request, 'core/user_profile.html', {'profile_user': profile_user})