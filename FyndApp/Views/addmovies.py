from django.shortcuts import render
from FyndApp.models import Movies





def movies(request):
    if request.method == 'GET':
        movies_obj = Movies.objects.all()
        return render(request,'addmovies.html',{'moviesobj':movies_obj})
