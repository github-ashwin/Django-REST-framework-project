from django.urls import path
from .views import PopularMoviesView
urlpatterns=[
    path('popular/', PopularMoviesView.as_view()),
    ]
