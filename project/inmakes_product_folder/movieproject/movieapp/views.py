from django.shortcuts import render
from .models import movie
# Create your views here.

def index(request):
    Movie = movie.objects.all()
    context = {
        'movie_list': Movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    Movie = movie.objects.get(id = movie_id)
    return render(request,"detail.html",{'movie':Movie})