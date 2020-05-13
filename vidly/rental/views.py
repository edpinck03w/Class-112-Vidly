from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
#MVC python manage.py runserver

#defining an endpoint
def index(request):
    all_movies = Movie.objects.all() # read Movie table to a list
    return render(request,'index.html', { 'title': 'Movies Catalog', 'movies': all_movies })
    #return HttpResponse("Hello World!!!")

def catalog(request):
    return render(request, 'catalog.html')

#about send your name
def about(request):
    return HttpResponse("Edward Pinckney")

def soon(request):
    return render(request, 'comingSoon.html')
    #return HttpResponse("Page coming soon, stay in touch :)")
