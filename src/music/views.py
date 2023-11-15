from rest_framework import viewsets
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

import json

from .models import *
from .serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
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
    
class PlayListsByUserIdViewSet(viewsets.ModelViewSet):

    queryset = PlayListsModel.objects.all()
    serializer_class = PlayListsSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = PlayListsModel.objects.filter(user_FUI=user_id).values()
        return queryset
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)
    
class PlayListTracksViewSet(viewsets.ModelViewSet):

    queryset = PlayListTracksModel.objects.all()
    serializer_class = PlayListsTracksSerializer
    pagination_class = StandardResultsSetPagination
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        track_id = kwargs.get('pk')
        try:  
            playlist_id = self.request.query_params.get('playlist_id')
            PlayListTracksModel.objects.filter(track_id=track_id, playlist_id=playlist_id).delete()
        except BaseException as e:
            return Response({"message": "Failed due to => {e}"})
        
        return Response({"message": "detail not found!"})
    
class TracksByPlayListIdViewSet(viewsets.ModelViewSet):
    
    queryset = TracksModel.objects.all()
    serializer_class = TracksSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        playlist_id = self.request.query_params.get('playlist_id')
        playlist_tracks = PlayListTracksModel.objects.filter(playlist_id=playlist_id).values("track_id")
        print(playlist_tracks)
        playlist_tracks_id = [track['track_id'] for track in playlist_tracks]
        queryset = TracksModel.objects.filter(id__in=playlist_tracks_id).values()
        return queryset
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)



class FavouritesViewSet(viewsets.ModelViewSet):

    queryset = FavouritesModel.objects.all()
    serializer_class = FavouritesSerializer
    pagination_class = StandardResultsSetPagination
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        track_id = kwargs.get('pk')
        try:  
            user_id = self.request.query_params.get('user_id')
            FavouritesModel.objects.filter(track_id=track_id, user_FUI=user_id).delete()
        except BaseException as e:
            return Response({"message": "Failed due to => {e}"})
        
        return Response({"message": "detail not found!"})
    
class FavouriteTracksByUserIdViewSet(viewsets.ModelViewSet):

    queryset = TracksModel.objects.all()
    serializer_class = TracksSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        fav_tracks = FavouritesModel.objects.filter(user_FUI=user_id).values('track_id')
        fav_tracks_id = [track['track_id'] for track in fav_tracks]
        queryset = TracksModel.objects.filter(id__in=fav_tracks_id).values()
        return queryset
    
    def list(self, request, *args, **kwargs):
        return Response(json.loads(json.dumps(super().list(request, *args, **kwargs).data))['results'], status=status.HTTP_200_OK)