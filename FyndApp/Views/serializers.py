from rest_framework import serializers
from FyndApp.models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movies
        fields = ('name','director','genre','score','popularity')
    

    
