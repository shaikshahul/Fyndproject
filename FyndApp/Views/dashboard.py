from FyndApp.models import Movies
from django.shortcuts import render
from datetime import datetime,timedelta
from django.db.models import Q
from django.core.serializers import serialize
from json import dumps
from django.http import JsonResponse



def dashboard(request):
    """dashboard view"""
    if request.method == "GET":
        today = datetime.now().date()
        playdate = today - timedelta(100)
        upcoming_date = today+timedelta(1)
        nowplayobj = Movies.objects.filter(release_date__range=[playdate, today])
        upcomobj = Movies.objects.filter(release_date__gte=upcoming_date)
        return render(request, "dashboard.html", {'nowplayobj':nowplayobj,
                                            'upcomobj':upcomobj})
                                            

def view_movies_deatils(request,pk):
    """show movie details"""
    if request.method == "GET":
        movie_obj = Movies.objects.get(id=int(pk))
        return render(request,"movieview.html",{'movieobj':movie_obj})

def search_movies(request):
    if request.method == 'GET':
        searchtext = request.GET.get('term')
        queryobj = Movies.objects.filter(Q(name__icontains=searchtext)|
                                         Q(director__icontains=searchtext)|
                                         Q(genre__icontains=searchtext)|
                                         Q(score__icontains=searchtext)|
                                         Q(popularity__icontains=searchtext)|
                                         Q(country__icontains=searchtext)|
                                         Q(language__icontains=searchtext)|
                                         Q(release_date__icontains=searchtext)
                                        )
        resp =list(map(lambda x: {'id': x.pk, 'value':x.name,
                              'director':x.director,
                              'genre':x.genre,
                              'language':x.language,
                              'year':x.release_date.year}, queryobj))
        if resp == []:
            return JsonResponse({'error':''})
        return JsonResponse(dumps(resp), safe=False)

