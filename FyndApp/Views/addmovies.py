from django.shortcuts import render,redirect
from FyndApp.models import Movies
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required, permission_required
import datetime



@login_required(login_url='/login')
def movies(request):
    """ view movies list"""
    if request.method == 'GET':
        movies_obj = Movies.objects.all()
        return render(request,'addmovies.html',{'moviesobj':movies_obj})
    elif request.method == 'POST':
        movieid = request.POST.get('movieid')
        name = request.POST.get('name')
        director = request.POST.get('director')
        popularity = request.POST.get('popularity')
        score = request.POST.get('score')
        language = request.POST.get('language')
        country = request.POST.get('country')
        youtube = request.POST.get('youtube')
        storyline = request.POST.get('storyline')
        image = request.FILES.get('image')
        releasedate =  request.POST.get('release_date')
        genre = request.POST.get('genre')
        ytube = youtube.split('=')
        if len(ytube) == 2:
            youtube_url = 'https://www.youtube.com/embed/{0}'.format(ytube[1])
        else:
            youtube_url = youtube
        if movieid:
            movobj = Movies.objects.get(id=int(movieid))
            if image:
                movobj.image = image
        else:
            movobj = Movies()
            movobj.image = image
        movobj.name = name
        movobj.director = director
        movobj.popularity = popularity
        movobj.score = score
        movobj.genre = genre
        movobj.language = language
        movobj.country = country
        movobj.youtube = youtube_url
        movobj.storyline = storyline
        movobj.release_date = datetime.datetime.strptime(
                releasedate, "%Y-%m-%d").date()
        movobj.save()
        return redirect('/movies/')
        # movie_content = render(
        #         request, '_partials/_addmovies.html', {'movie_obj': [movobj]}).content
        # return JsonResponse({'moviobj': movobj.id, 'movie_content': movie_content})

        
@login_required(login_url='/login')
def movie_edit(request,idd):
    """Edit the movie details """
    if request.method == "GET":
        movieobj = Movies.objects.get(id=int(idd))
        serobj = serialize('json',[movieobj])
        return JsonResponse({'editobj':serobj})




        
        



