from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


@ api_view(["GET"])
def director_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)

@api_view(["GET"])
def director_detail_view(request, **kwargs):
    director = Director.objects.get(id=kwargs['id'])
    data = DirectorSerializer(director, many=False).data
    return Response(data=data)

@api_view(["GET"])
def movie_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)

@api_view(["GET"])
def movie_detail_view(request, **kwargs):
    movie = Movie.objects.get(id=kwargs['id'])
    data = MovieSerializer(movie, many=False).data
    return Response(data=data)

@api_view(["GET"])
def review_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)

@api_view(["GET"])
def review_detail_view(request, **kwargs):
    review = Review.objects.get(id=kwargs['id'])
    data = ReviewSerializer(review, many=False).data
    return Response(data=data)

@api_view(["GET"])
def movies_reviews_view(reques):
    movies = Movie.objects.all()
    serializer = MoviesReviewsSerializer(movies, many=True)
    return Response(data=serializer.data)