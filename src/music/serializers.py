from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistsModel
        fields = '__all__'
        
class AlbumsSerializer(serializers.ModelSerializer):
    artist_name = serializers.SerializerMethodField()
    
    class Meta:
        model = AlbumsModel
        fields = '__all__'
        
    def get_artist_name(self, obj):
        return obj.artist_id.artist_name if obj.artist_id else None

class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenresModel
        fields = '__all__'

class TracksSerializer(serializers.ModelSerializer):
    artist_name = serializers.SerializerMethodField()
    
    class Meta:
        model = TracksModel
        fields = '__all__'
    
    def get_artist_name(self, obj):
        return obj.artist_id.artist_name if obj.artist_id else None

class PlayListsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayListsModel
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayListsModel.objects.all(),
                fields=['playlist_name', 'user_FUI']
            )
        ]

class PlayListsTracksSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayListTracksModel
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayListTracksModel.objects.all(),
                fields=['playlist_id', 'track_id']
            )
        ]

class FavouritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavouritesModel
        fields = ['id', 'track_id', 'user_FUI']

        validators = [
            UniqueTogetherValidator(
                queryset=FavouritesModel.objects.all(),
                fields=['track_id', 'user_FUI']
            )
        ]