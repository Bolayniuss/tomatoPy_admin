from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.authentication import TokenAuthentication

from .models import TvShow
from .serializers import TvShowSerializer


# dev Token: 9e29971eebfdd1e7180eabb3f4b1545333a78fbd9fa10e3d6c8a84155a33fe55s
class TvShowListView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    model = TvShow
    serializer_class = TvShowSerializer

    def get_queryset(self):
        return TvShow.objects.filter(client__id=self.request.user.id).select_related("tvshow")