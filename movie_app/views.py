from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


@ api_view(["GET", "POST"])
def director_view(request):
    if request.method == "GET":
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        name = request.data.get("name")
        director = Director.objects.create(name=name)
        director.save()
        return Response(data={"message": "Director created successfully!"},
                        status=status.HTTP_201_CREATED)



@api_view(["GET", "PUT", "DELETE"])
def director_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Director not found'})
    if request.method == "GET":
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        director.name = request.data.get("name")
        director.save()
        return Response(data={'massage': "Director updated successfully!",
                              'director': DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)

@api_view(["GET", "POST"])
def movie_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        title = request.data.get("title")
        description = request.data.get("description")
        duration = request.data.get("duration")
        director = request.data.get("director")
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director)
        movie.save()
        return Response(data={"massage": "Movie created successfully!",
                              "movie": MovieSerializer(movie).data},
                        status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def movie_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found'})
    if request.method == "GET":
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        movie.title = request.data.get("title")
        movie.description = request.data.get("description")
        movie.duration = request.data.get("duration")
        movie.director_id = request.data.get("director")
        movie.save()
        return Response(data={"massage": "Movie updated successfully!",
                              "movie": MovieSerializer(movie).data},
                        status=status.HTTP_201_CREATED)

@api_view(["GET", "POST"])
def review_view(request):
    try:
        reviews = Review.objects.all()
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': "Review not found"})
    if request.method == "GET":
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        text = request.data.get("text")
        stars = request.data.get("stars")
        movie = request.data.get("movie")
        reviews = Review.objects.create(text=text, stars=stars, movie_id=movie)
        reviews.save()
        return Response(data={"massage": "Review created successfully!",
                              "reviews": ReviewSerializer(reviews).data},
                        status=status.HTTP_201_CREATED)



@api_view(["GET", "PUT", "DELETE"])
def review_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Review not found"})
    if request.method == "GET":
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        review.text = request.data.get("text")
        review.stars = request.data.get("stars")
        review.movie_id = request.data.get("movie")
        review.save()
        return Response(data={"massage": "Review updated successfully!",
                              "review": ReviewSerializer(review).data},
                        status=status.HTTP_201_CREATED)

@api_view(["GET"])
def movies_reviews_view(reques):
    movies = Movie.objects.all()
    serializer = MoviesReviewsSerializer(movies, many=True)
    return Response(data=serializer.data)