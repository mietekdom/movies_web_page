from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('info', 'name', 'description', 'year', 'released', 'imdb_rating')