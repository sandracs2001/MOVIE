from django.shortcuts import render
from movies.models import Movies

app_name = 'movies'

def home(request):
    f = Movies.objects.all()
    return render(request,'home.html',{'f':f})
