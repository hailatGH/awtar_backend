import os
from io import BytesIO
from django.db import models
from PIL import Image, ImageOps
from django.core.files import File
from django.core.exceptions import ValidationError


def validate_image_extension(value):
    if value is None:
        return
    # [0] returns path+filename; [1] returns .extention
    ext = os.path.splitext(value.name)[1]
    # list of valid extentions for image
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension for an image!')


def validate_track_extension(value):
    # pass
    if value is None:
        return
    # [0] returns path+filename; [1] returns .extention
    ext = os.path.splitext(value.name)[1]
    # list of valid extentions for audio
    valid_extensions = ['.aac', '.mp3', '.wav']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension for an audio file!')


def Artists_Profile_Images(instance, filename):
    return '/'.join(['Media_Files', 'Artists_Profile_Images', str(filename)])


def Albums_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Albums_Cover_Images', str(filename)])


def Genres_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Genres_Cover_Images', str(filename)])


def Track_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Tracks_Cover_Images', str(filename)])


def Track_Files(instance, filename):
    return '/'.join(['Media_Files', 'Tracks_Audio_Files', str(filename)])


class ArtistsModel(models.Model):

    class Meta:
        ordering = ['id']

    artist_name = models.CharField(null=False, blank=True, max_length=256)
    artist_title = models.CharField(null=True, blank=True, max_length=256)
    artist_rating = models.IntegerField(null=True, blank=True, default=0)
    artist_status = models.BooleanField(null=False, blank=True, default=False)
    artist_releaseDate = models.DateField(null=True, blank=True)
    artist_description = models.CharField(
        null=True, blank=True, max_length=4096)
    artist_viewcount = models.IntegerField(null=False, blank=True, default=0)
    # artist_FUI = models.CharField(
    #     null=False, blank=True, unique=True, max_length=1023)
    encoder_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artist_profileImage = models.ImageField(null=False, blank=True, upload_to=Artists_Profile_Images, validators=[
        validate_image_extension])

    def save(self, *args, **kwargs):
        image = Image.open(self.artist_profileImage)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(
            image_io, name=str(self.artist_profileImage))
        self.artist_profileImage = compressed_image
        super(ArtistsModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}: {self.artist_name}"


class AlbumsModel(models.Model):

    class Meta:
        ordering = ['id']

    album_name = models.CharField(null=False, blank=True, max_length=256)
    album_rating = models.IntegerField(null=True, blank=True, default=0)
    album_status = models.BooleanField(null=False, blank=True, default=False)
    album_releaseDate = models.DateField(null=True, blank=True)
    album_description = models.CharField(
        null=True, blank=True, max_length=4096)
    album_viewcount = models.IntegerField(null=False, blank=True, default=0)
    album_price = models.IntegerField(null=False, blank=True, default=40)
    artist_id = models.ForeignKey(ArtistsModel, related_name="albumasartist",
                                  related_query_name="albumasartistquery", null=False, blank=True, on_delete=models.DO_NOTHING)
    encoder_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    album_coverImage = models.ImageField(null=False, blank=True, upload_to=Albums_Cover_Images, validators=[
        validate_image_extension])

    def save(self, *args, **kwargs):
        image = Image.open(self.album_coverImage)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(image_io, name=str(self.album_coverImage))
        self.album_coverImage = compressed_image
        super(AlbumsModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}: {self.album_name}"


class GenresModel(models.Model):

    class Meta:
        ordering = ['id']

    genre_name = models.CharField(null=False, blank=True, max_length=256)
    genre_rating = models.IntegerField(null=True, blank=True, default=0)
    genre_status = models.BooleanField(null=False, blank=True, default=False)
    genre_description = models.CharField(
        null=True, blank=True, max_length=4096)
    genre_viewcount = models.IntegerField(null=False, blank=True, default=0)
    encoder_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genre_coverImage = models.ImageField(null=False, blank=True, upload_to=Genres_Cover_Images, validators=[
        validate_image_extension])

    def save(self, *args, **kwargs):
        image = Image.open(self.genre_coverImage)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(image_io, name=str(self.genre_coverImage))
        self.genre_coverImage = compressed_image
        super(GenresModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}: {self.genre_name}"


class TracksModel(models.Model):

    class Meta:
        ordering = ['id']

    track_name = models.CharField(null=False, blank=True, max_length=256)
    track_rating = models.IntegerField(null=True, blank=True, default=0)
    track_status = models.BooleanField(null=False, blank=True, default=False)
    track_releaseDate = models.DateField(null=True, blank=True)
    track_description = models.CharField(
        null=True, blank=True, max_length=4096)
    track_viewcount = models.IntegerField(null=False, blank=True, default=0)

    track_lyrics = models.CharField(null=True, blank=True, max_length=4096)
    track_price = models.IntegerField(null=False, blank=True, default=5)
    artist_id = models.ForeignKey(ArtistsModel, related_name="trackasartist",
                                  related_query_name="trackasartistquery", null=False, blank=True, on_delete=models.DO_NOTHING)
    album_id = models.ForeignKey(AlbumsModel, related_name="trackasalbum",
                                 related_query_name="trackasalbumquery", null=True, blank=True, on_delete=models.DO_NOTHING)
    genre_id = models.ForeignKey(GenresModel, related_name="genre_tracks",
                                 related_query_name="genre_tracks", null=False, blank=True, on_delete=models.DO_NOTHING)
    encoder_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    track_coverImage = models.ImageField(null=False, blank=True, upload_to=Track_Cover_Images, validators=[
        validate_image_extension])
    track_audioFile = models.FileField(null=False, blank=True, upload_to=Track_Files, validators=[
        validate_track_extension])

    def save(self, *args, **kwargs):
        image = Image.open(self.track_coverImage)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(image_io, name=str(self.track_coverImage))
        self.track_coverImage = compressed_image
        super(TracksModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}: {self.track_name}"


class PlayListsModel(models.Model):

    class Meta:
        ordering = ['id']

    playlist_name = models.CharField(null=False, blank=True, max_length=256)
    user_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.playlist_name}"


class PlayListTracksModel(models.Model):

    class Meta:
        ordering = ['id']

    playlist_id = models.ForeignKey(
        PlayListsModel, null=False, blank=True, on_delete=models.CASCADE)
    track_id = models.ForeignKey(TracksModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.playlist_id} <--> {self.track_id}"


class FavouritesModel(models.Model):

    class Meta:
        ordering = ['id']

    track_id = models.ForeignKey(
        TracksModel, null=False, blank=True, on_delete=models.CASCADE, related_name='tracks')
    user_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.user_FUI} <--> {self.track_id}"
