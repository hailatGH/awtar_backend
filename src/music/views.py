from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import json
from datetime import datetime
from itertools import chain

from .models import *
from .serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'


class ArtistsViewSet(viewsets.ModelViewSet):

    queryset = ArtistsModel.objects.all()
    serializer_class = ArtistsSerializer
    pagination_class = StandardResultsSetPagination
    
class AlbumsViewSet(viewsets.ModelViewSet):

    queryset = AlbumsModel.objects.all()
    serializer_class = AlbumsSerializer
    pagination_class = StandardResultsSetPagination
    
class GenresViewSet(viewsets.ModelViewSet):

    queryset = GenresModel.objects.all()
    serializer_class = GenresSerializer
    pagination_class = StandardResultsSetPagination
    
class TracksViewSet(viewsets.ModelViewSet):

    queryset = GenresModel.objects.all()
    serializer_class = GenresSerializer
    pagination_class = StandardResultsSetPagination
    
class PlayListsViewSet(viewsets.ModelViewSet):

    queryset = PlayListsModel.objects.all()
    serializer_class = PlayListsSerializer
    pagination_class = StandardResultsSetPagination
    
class PlayListTracksViewSet(viewsets.ModelViewSet):

    queryset = PlayListTracksModel.objects.all()
    serializer_class = PlayListsTracksSerializer
    pagination_class = StandardResultsSetPagination
    
class FavouritesViewSet(viewsets.ModelViewSet):

    queryset = FavouritesModel.objects.all()
    serializer_class = FavouritesSerializer
    pagination_class = StandardResultsSetPagination