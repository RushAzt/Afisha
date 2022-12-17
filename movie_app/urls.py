from django.urls import path
from .views import *

urlpatterns = [
    path('directors/', director_view),
    path('directors/<int:id>/', director_detail_view),
    path('movies/', movie_view),
    path('movies/<int:id>/', movie_detail_view),
    path('reviews/', review_view),
    path('reviews/<int:id>/', review_detail_view),
    path('movies/reviews/', movies_reviews_view)
]