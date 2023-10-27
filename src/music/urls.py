from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ArtistsViewSet, AlbumsViewSet, GenresViewSet, TracksViewSet, PlayListsViewSet, PlayListTracksViewSet, FavouritesViewSet,
    AlbumsByArtistIdViewSet, SingleTracksByArtistIdViewSet, TracksByAlbumIdViewSet, TracksByGenreIdViewSet, FavouriteTracksByUserIdViewSet,
    TracksByPlayListIdViewSet, PlayListsByUserIdViewSet)

router = DefaultRouter(trailing_slash=False)
router.register(r'artists', ArtistsViewSet, basename="artists")
router.register(r'albumsbyartistid', AlbumsByArtistIdViewSet,
                basename="albumsbyartistid")
router.register(r'singletracksbyartistid',
                SingleTracksByArtistIdViewSet, basename="singletracksbyartistid")

router.register(r'albums', AlbumsViewSet, basename="albums")
router.register(r'tracksbyalbumid', TracksByAlbumIdViewSet, basename="tracksbyalbumid")


router.register(r'genres', GenresViewSet, basename="genres")
router.register(r'tracksbygenreid', TracksByGenreIdViewSet, basename="tracksbygenreid")

router.register(r'tracks', TracksViewSet, basename="tracks")

router.register(r'playlists', PlayListsViewSet, basename="playlists")
router.register(r'playlistsbyuserid', PlayListsByUserIdViewSet, basename="playlistsbyuserid")
router.register(r'playlisttracks', PlayListTracksViewSet,
                basename="playlisttracks")
router.register(r'tracksbyplaylistid', TracksByPlayListIdViewSet,
                basename="tracksbyplaylistid")

router.register(r'favourites', FavouritesViewSet, basename="favourites")
router.register(r'favouritetracksbyuserid', FavouriteTracksByUserIdViewSet, basename="favouritetracksbyuserid")

urlpatterns = [
    path('', include(router.urls))
]
