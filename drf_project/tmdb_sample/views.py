from django.shortcuts import render
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import MovieSerializer
# Create your views here.

class PopularMoviesView(APIView):
    def get(self, request):
        page = request.query_params.get('page', 1) #Fetch Page Number

        url = f"{settings.TMDB_BASE_URL}/movie/popular?api_key={settings.TMDB_API_KEY}&page={page}" #Construct URL

        response = requests.get(url) #GET request

        if response.status_code == 200:
            data = response.json()

            movies = data.get('results',[])
            serialized_movies = MovieSerializer(movies, many=True).data #Converting raw data 

            return Response({'results': serialized_movies,'total_pages': data['total_pages']}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to fetch data from TMDb'}, status=status.HTTP_400_BAD_REQUEST)
    

