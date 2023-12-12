from django.shortcuts import render
from django.shortcuts import redirect
from movies.models import Movies
from movies.forms import MovieForm



def update(request,p):
    b = Movies.objects.get(id=p)
    if (request.method == "POST"):
        form = MovieForm(request.POST, request.FILES, instance=b)
        if form.is_valid():
            form.save()
            return home(request)

    form = MovieForm(instance=b)
    return render(request, 'update.html', {'b': form})


def delete(request,p):
    b = Movies.objects.get(id = p)
    b.delete()
    return home(request)


def home(request):
    f = Movies.objects.all()
    return render(request,'home.html',{'f':f})

def somewhere(request,p):
    f = Movies.objects.get(id=p)
    return render(request,'somewhere page.html',{'f':f})

def areyousure(request,p):
    f = Movies.objects.get(id=p)
    return render(request,'areyousure.html',{'f':f})

def add(request):
    if (request.method == "POST"):
        T = request.POST['T']
        A = request.POST['A']
        q = request.FILES['i']
        b = Movies.objects.create(img=q, des=A, name=T)
        b.save()
        return home(request)
    return render(request, 'add.html', {'n': 'john', 's': 'san'})