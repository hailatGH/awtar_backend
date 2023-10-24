from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArtistsViewSet, AlbumsViewSet, GenresViewSet, TracksViewSet, PlayListsViewSet, PlayListTracksViewSet, FavouritesViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'artists', ArtistsViewSet, basename="artists")
router.register(r'albums', AlbumsViewSet, basename="albums")
router.register(r'genres', GenresViewSet, basename="genres")
router.register(r'tracks', TracksViewSet, basename="tracks")
router.register(r'playlists', PlayListsViewSet, basename="playlists")
router.register(r'playlisttracks', PlayListTracksViewSet, basename="playlisttracks")
router.register(r'favourites', FavouritesViewSet, basename="favourites")

urlpatterns = [
    path('', include(router.urls))
]
