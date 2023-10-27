from rest_framework import viewsets
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

import json

from .models import *
from .serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'

class ArtistsViewSet(viewsets.ModelViewSet):

    queryset = ArtistsModel.objects.all()
    serializer_class = ArtistsSerializer
    pagination_class = StandardResultsSetPagination
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)
    
class AlbumsByArtistIdViewSet(viewsets.ModelViewSet):

    queryset = AlbumsModel.objects.all()
    serializer_class = AlbumsSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        artist_id = self.request.query_params.get('artist_id')
        queryset = self.queryset.filter(artist_id=artist_id)
        return queryset
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)

class SingleTracksByArtistIdViewSet(viewsets.ModelViewSet):
    
    queryset = TracksModel.objects.all()
    serializer_class = TracksSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        artist_id = self.request.query_params.get('artist_id')
        queryset = self.queryset.filter(artist_id=artist_id, album_id=None)
        return queryset
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)




class AlbumsViewSet(viewsets.ModelViewSet):

    queryset = AlbumsModel.objects.all()
    serializer_class = AlbumsSerializer
    pagination_class = StandardResultsSetPagination
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)
    
class TracksByAlbumIdViewSet(viewsets.ModelViewSet):

    queryset = TracksModel.objects.all()
    serializer_class = TracksSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        album_id = self.request.query_params.get('album_id')
        queryset = self.queryset.filter(album_id=album_id).filter(album_id= not None)
        return queryset
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)




class GenresViewSet(viewsets.ModelViewSet):

    queryset = GenresModel.objects.all()
    serializer_class = GenresSerializer
    pagination_class = StandardResultsSetPagination
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)
    
class TracksByGenreIdViewSet(viewsets.ModelViewSet):

    queryset = TracksModel.objects.all()
    serializer_class = TracksSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        genre_id = self.request.query_params.get('genre_id')
        queryset = self.queryset.filter(genre_id=genre_id)
        return queryset
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)




class TracksViewSet(viewsets.ModelViewSet):

    queryset = TracksModel.objects.all()
    serializer_class = TracksSerializer
    pagination_class = StandardResultsSetPagination
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)




    
class PlayListsViewSet(viewsets.ModelViewSet):

    queryset = PlayListsModel.objects.all()
    serializer_class = PlayListsSerializer
    pagination_class = StandardResultsSetPagination
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)
    
class PlayListTracksViewSet(viewsets.ModelViewSet):

    queryset = PlayListTracksModel.objects.all()
    serializer_class = PlayListsTracksSerializer
    pagination_class = StandardResultsSetPagination
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)




class FavouritesViewSet(viewsets.ModelViewSet):

    queryset = FavouritesModel.objects.all()
    serializer_class = FavouritesSerializer
    pagination_class = StandardResultsSetPagination
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)
    
class FavouriteTracksByUserIdViewSet(viewsets.ModelViewSet):

    queryset = TracksModel.objects.all()
    serializer_class = TracksSerializer
    pagination_class = StandardResultsSetPagination
    
    # def get_queryset(self):
        # from django.db.models import Value
        
        # user_id = self.request.query_params.get('user_id')
        # fav_tracks = FavouritesModel.objects.filter(user_FUI=user_id).values('id', 'track_id')
        # queryset = []
        # fav_id_track_id = [{"fav_id": track['id'], "track_id": track['track_id']} for track in fav_tracks]
        # for track in fav_id_track_id:
        #     track_obj = TracksModel.objects.filter(id=track['track_id']).annotate(fav_id=Value(track['fav_id'])).first()
        #     queryset.append(track_obj)
        # return queryset
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)