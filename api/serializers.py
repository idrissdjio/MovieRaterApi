from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Movie, Rating
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """serialize the user model"""
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        """
        as the password will be saved without hashing,
         we will override it to be hashed
        """
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class MovieSerializer(serializers.ModelSerializer):
    """serialize the movie model"""
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    """serialize the rating model"""
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')
