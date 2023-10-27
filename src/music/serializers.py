from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistsModel
        fields = '__all__'
        
class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumsModel
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenresModel
        fields = '__all__'

class TracksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TracksModel
        fields = '__all__'

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
    tracks = TracksSerializer(many=True)

    class Meta:
        model = FavouritesModel
        fields = ['id', 'track_id', 'user_FUI', 'tracks']

    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset=FavouritesModel.objects.all(),
    #             fields=['track_id', 'user_FUI']
    #         )
    #     ]
        
    # def get_nested_relationships(self, instance):
    #     # Custom method to retrieve nested relationships
    #     # You can implement your logic here to fetch the related nested objects

    #     # Example: Fetch the related tracks for the favourite instance
    #     tracks = instance.tracks.all()

    #     # Serialize the related tracks using the TrackSerializer
    #     track_serializer = TracksSerializer(tracks, many=True)
    #     serialized_tracks = track_serializer.data

    #     return serialized_tracks

    # def to_representation(self, instance):
    #     # Override the to_representation method to include nested relationships
    #     representation = super().to_representation(instance)

    #     # Fetch and include the nested relationships
    #     nested_relationships = self.get_nested_relationships(instance)
    #     representation['tracks'] = nested_relationships

    #     return representation