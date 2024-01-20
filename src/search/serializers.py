from rest_framework import serializers
from music.models import *

class ArtistsSerializer(serializers.ModelSerializer):
    # artist_profileImage= serializers.SerializerMethodField()
    number_of_tracks = serializers.SerializerMethodField()
    number_of_albums = serializers.SerializerMethodField()
    # is_singer = serializers.SerializerMethodField()
    class Meta:
        model = ArtistsModel
        fields = '__all__'

    # def get_artist_profileImage(self, obj):
    #     artist_profileImage = obj.artist_profileImage.url
    #     # artist_profileImage = "https://awtarstoragev100.blob.core.windows.net/awtarstorage/media" + artist_profileImage # replace adjust_artist_profileImage with your custom function
    #     return artist_profileImage
    
    def get_number_of_albums(self,obj):
        id = obj.id
        number_of_albums=AlbumsModel.objects.filter(artist_id=id).count()
        return number_of_albums
    
    def get_number_of_tracks(self,obj):
        id = obj.id
        number_of_tracks =TracksModel.objects.filter(artist_id=id).count()
        return number_of_tracks
    
    # def get_is_singer(self,obj):
    #     id = obj.id
    #     is_singer=TrackDetailModel.objects.filter(artist_id=id,privilege="singer").exists()
    #     return is_singer

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.queryset = self.queryset.exclude(is_singer=False,artist_status=False)
class AlbumsSerializer(serializers.ModelSerializer):
    # album_coverImage= serializers.SerializerMethodField()
    artist_name = serializers.SerializerMethodField()
    # is_purchasedByUser = serializers.SerializerMethodField()
    number_of_tracks = serializers.SerializerMethodField()
    # album_viewcount = serializers.SerializerMethodField()
    class Meta:
        model = AlbumsModel
        fields = '__all__'

    # def get_album_coverImage(self, obj):
    #     album_coverImage = obj.album_coverImage
    #     # album_coverImage = "https://zemamultimediablobcdn.azureedge.net/zemacontainer/" + album_coverImage # replace adjust_artist_profileImage with your custom function
    #     return album_coverImage
    
    
    # def get_artist_name (self,obj):
    #     artist_objects = obj.artist_id.all()
    #     artist_names = [artist.artist_name for artist in artist_objects]
    #     return artist_names
    def get_artist_name (self,obj):
        artist_names = obj.artist_id.artist_name
        # artist_objects = obj.artist_id.all()
        # artist_names = [artist.artist_name for artist in artist_objects]
        return artist_names
    
    # def get_is_purchasedByUser(self,obj):
    #     album_id =obj.id
    #     user_id = self.context.get('user_id')
    #     is_purchasedByUser=PurchasedAlbumsModel.objects.filter(album_id = album_id, user_FUI=user_id).exists()
    #     return is_purchasedByUser
    
    def get_number_of_tracks(self,obj):
        id = obj.id
        number_of_tracks =TracksModel.objects.filter(album_id=id).count()
        return number_of_tracks
    
    # def get_album_viewcount(self, obj):
    #         id = obj.id
    #         try:
    #             viewCount = AlbumsViewCount.objects.filter(
    #                 album_id=id).values("album_viewcount").first()
    #             if viewCount:
    #                 album_viewcount = viewCount['album_viewcount']
    #             else:
    #                 album_viewcount = 0
    #         except:
    #             album_viewcount = 0
    #         return album_viewcount

   
class TracksSerializer(serializers.ModelSerializer):
    # track_coverImage= serializers.SerializerMethodField()
    # track_audioFile= serializers.SerializerMethodField()
    artist_name = serializers.SerializerMethodField()
    # is_purchasedByUser = serializers.SerializerMethodField()
    # track_viewcount = serializers.SerializerMethodField()

    class Meta:
        model = TracksModel
        fields = '__all__'

    # def get_track_coverImage(self, obj):
    #     track_coverImage = obj.track_coverImage
    #     # track_coverImage = "https://zemamultimediablobcdn.azureedge.net/zemacontainer/" + track_coverImage # replace adjust_artist_profileImage with your custom function
    #     return track_coverImage
    
    # def get_track_audioFile(self, obj):
    #     track_audioFile = obj.track_coverImage
    #     # track_audioFile = "https://zemamultimediablobcdn.azureedge.net/zemacontainer/" + track_audioFile # replace adjust_artist_profileImage with your custom function
    #     return track_audioFile
    
    def get_artist_name (self,obj):
        artist_names = obj.artist_id.artist_name
        # artist_objects = obj.artist_id.all()
        # artist_names = [artist.artist_name for artist in artist_objects]
        return artist_names

    # def get_is_purchasedByUser(self,obj):
    #     track_id =obj.id
    #     user_id = self.context.get('user_id')
    #     is_purchasedByUser=PurchasedTracksModel.objects.filter(track_id = track_id, user_FUI=user_id).exists()
    #     return is_purchasedByUser
    
    # def get_track_viewcount(self, obj):
    #     id = obj.id
    #     try:
    #         viewCount = TracksViewCount.objects.filter(
    #             track_id=id).values("track_viewcount").first()
    #         if viewCount:
    #             track_viewcount = viewCount['track_viewcount']
    #         else:
    #             track_viewcount = 0
    #     except:
    #         track_viewcount = 0
    #     return track_viewcount