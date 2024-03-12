from django.shortcuts import render, redirect
from .models import Movie
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def sign_up_page(request):
    if request.method == "POST":
       form = NewUserForm(request.POST)
       if form.is_valid():
           user = form.save()
           return redirect("login_page")
    else:
        form = NewUserForm()
    return render(request, "sign_up.html", {
        'form': form
    })

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {
        'form': form
    })

def logout_action(request):
    logout(request)
    return redirect('home_page')

def movies_page(request):
    title = request.GET.get('title')
    if title:
        if len(title) > 0:
            movies = Movie.objects.filter(title__icontains=title)
        else:
            movies = Movie.objects.none()
    else:
        movies = Movie.objects.none()
    movies1 = Movie.objects.all()[:4]
    movies2 = Movie.objects.all()[4:8]
    movies3 = Movie.objects.all()[8:12]
    movies4 = Movie.objects.all()[12:16]
    return render(request, 'movies.html', {'movies1': movies1, 'movies2': movies2, 'movies3': movies3, 'movies4': movies4, 'movies': movies })

def top_page(request):
    top_movies = Movie.objects.order_by('-rate')[:5]
    return render(request, 'top.html', {'top_movies': top_movies})
  


def movie_detail_page(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies_detail.html', {'movie': movie })

def home_page(request):
    return render(request, 'index.html')
# Create your views here.