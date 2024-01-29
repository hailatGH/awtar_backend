from rest_framework.routers import DefaultRouter

from search_app.views import *

searchrouter = DefaultRouter(trailing_slash=False)
searchrouter.register(r'track',  TrackViewSet, basename="track")
searchrouter.register(r'album',  AlbumViewSet, basename="album")
searchrouter.register(r'artist',  ArtistViewSet, basename="artist")