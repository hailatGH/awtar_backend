# Generated by Django 4.2.6 on 2023-10-24 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistsmodel',
            name='artist_FUI',
        ),
    ]
