from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, director):
        return director.movie_count()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'id title description duration director rating'.split()

    def get_rating(self, movie):
        return movie.rating()
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars stars_str movie'.split()
class MoviesReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'id rating title description duration director reviews movie'.split()
    def get_rating(self, movie):
        return movie.rating()

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, name):
        name_exists = Director.objects.filter(name=name).exists()
        if not name_exists:
            return name
        raise ValidationError('Director already exists!')
class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)
    director = serializers.IntegerField(required=True, min_value=1)

    def validate_title(self, title):
        title_exists = Movie.objects.filter(title=title).exists()
        if not title_exists:
            return title
        raise ValidationError('Movies with this title already exists')

    def validate_director(self, director):

        if Director.objects.filter(id=director).count() == 0:
            raise ValidationError('Director with that id does not exists!')
        return director

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    stars = serializers.IntegerField(min_value=1, max_value=5, required=True)
    movie_id = serializers.IntegerField(min_value=1, required=True)

    def validate_movie_id(self, movie_id):
        movie_exists = Movie.objects.filter(id=movie_id).exists()
        if movie_exists:
            return movie_id
        raise ValidationError('Movie with this id does not exist')


