from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#MVC python manage.py runserver

#defining an endpoint
def index(request):
    return HttpResponse("Hello World!!!")


#about send your name
def about(request):
    return HttpResponse("Edward Pinckney")

def soon(request):
    return HttpResponse("Page coming soon, stay in touch :)")
