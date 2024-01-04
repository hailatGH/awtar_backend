from django.db.models import Q ,Exists, OuterRef
from django.contrib.postgres.search import TrigramSimilarity, SearchQuery, SearchRank, SearchVector

from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response

from music.models import *
from .serializers import *

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = ArtistsModel.objects.all()
    serializer_class = ArtistsSerializer
    def get_queryset(self):
        queryset = ArtistsModel.objects.all()
        
        # is_singer = Exists(TrackDetailModel.objects.filter(artist_id=OuterRef('pk'), privilege="singer"))
        # queryset = ArtistsModel.objects.annotate(is_singer=is_singer)
        
        return queryset.exclude(artist_status=False)
    @action(detail=False, methods=['GET'])
    def search(self, request):
        query = request.query_params.get('q', '')
        user_id = request.query_params.get('UID', '')
        search_vector = SearchVector('artist_name', 'artist_description', 'albumasartistquery__album_name', 'albumasartistquery__album_description')
        search_query = SearchQuery(query)
        results = self.get_queryset().annotate(
            rank=SearchRank(search_vector, search_query) + TrigramSimilarity('artist_name', query) + TrigramSimilarity('artist_description', query),
        ).filter(Q(rank__gte=0.1)).distinct().order_by('-rank','id')
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)
    

    def create(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def retrieve(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def update(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def partial_update(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def destroy(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def list(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = AlbumsModel.objects.all()
    serializer_class = AlbumsSerializer
    def get_queryset(self):
        queryset = AlbumsModel.objects.all()
        return queryset.exclude(album_status=False)
    @action(detail=False, methods=['GET'])
    def search(self, request):
        query = request.query_params.get('q', '')
        user_id = request.query_params.get('UID', '')
        search_vector = SearchVector('album_name', 'album_description', 'artist_id__artist_name', 'artist_id__artist_description')
        search_query = SearchQuery(query)
        results = self.get_queryset().annotate(
            rank=SearchRank(search_vector, search_query) + TrigramSimilarity('album_name', query) + TrigramSimilarity('album_description', query) + TrigramSimilarity('artist_id__artist_name', query) + TrigramSimilarity('artist_id__artist_description', query),
        ).distinct().filter(Q(rank__gte=0.1)).order_by('-rank','id')
        serializer = self.get_serializer(results, many=True,context={'user_id': user_id})
        return Response(serializer.data)
    
    
    def create(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def retrieve(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def update(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def partial_update(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def destroy(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def list(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )
   

class TrackViewSet(viewsets.ModelViewSet):
    queryset = TracksModel.objects.all()
    serializer_class = TracksSerializer
    def get_queryset(self):
        queryset = TracksModel.objects.all()
        return queryset.exclude(track_status=False)
    @action(detail=False, methods=['GET'])
    def search(self, request):
        query = request.query_params.get('q', '')
        user_id = request.query_params.get('UID', '')
        search_vector = SearchVector('track_name', 'track_description', 'artist_id__artist_name', 'artist_id__artist_description', 'album_id__album_name', 'album_id__album_description')
        search_query = SearchQuery(query)
        results = self.get_queryset().annotate(
            rank=SearchRank(search_vector, search_query) + TrigramSimilarity('track_name', query) + TrigramSimilarity('track_description', query)+ TrigramSimilarity('artist_id__artist_name', query) + TrigramSimilarity('artist_id__artist_description', query)+ TrigramSimilarity('album_id__album_name', query) + TrigramSimilarity('album_id__album_description', query)+ TrigramSimilarity('genre_id__genre_description', query)+ TrigramSimilarity('genre_id__genre_name', query),
        ).filter(Q(rank__gte=0.1)).distinct().order_by('-rank','id')
        serializer = self.get_serializer(results, many=True,context={'user_id': user_id})
        return Response(serializer.data)
    

    def create(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def retrieve(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def update(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def partial_update(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def destroy(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

    def list(self, request, *args, **kwargs):
        return Response(
                    {
                        "message": "Not allowed!!",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )
