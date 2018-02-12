from django.conf.urls import url
from FyndApp.Views.dashboard import dashboard,view_movies_deatils,search_movies
from FyndApp.Views.addmovies import movies,movie_edit
from FyndApp.Views.loginpage import signup,logout_user,login_user



urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^movies/$', movies, name='movies'),
    url(r'^movie/(?P<pk>\w+)/view/$', view_movies_deatils, name='view_movies_deatils'),
    url(r'^search/$', search_movies, name='search_movies'),
    url(r'^movie/(?P<idd>\w+)/edit/$', movie_edit, name='movie_edit'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^logout/$', logout_user, name='logout_user'),
    url(r'^login/$', login_user, name='login_user'),





]