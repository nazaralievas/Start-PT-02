from django.shortcuts import render
from django.shortcuts import redirect
from .models import Movie
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
            comment.movie = movie
            comment.save()
            return redirect('movie_detail', id=movie.id)
    return render(request, 'core/movie_detail.html', {'movie': movie, 'form': form})


def rules(request):
    return render(request, 'core/rules.html')