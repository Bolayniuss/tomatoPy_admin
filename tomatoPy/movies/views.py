from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView

from accounts.authentication import TokenAuthentication

from .models import Movie, MovieRegistration
from .serializers import MovieSerializer


class MovieAPIListView(ListCreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    model = Movie
    serializer_class = MovieSerializer

    def get_queryset(self):
        movies = set()
        query = MovieRegistration.objects.filter(client__id=self.request.user.id)
        if self.request.query_params.get('all', '0') == '0':
            query = query.filter(synchronized=False)
        for mr in query:
            movies.add(mr.movie)
        return movies
