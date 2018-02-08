from django.conf.urls import url
from FyndApp.Views.index import dashboard
from FyndApp.Views.addmovies import movies



urlpatterns = [
    url(r'^$', dashboard, name='dashboard_admin'),
    url(r'^movies/$', movies, name='movies'),
]