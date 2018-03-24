# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import CharField, Model
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Song(Model):
    """
    Song Model. ID field is created auto.
    """
    title = CharField(max_length=64)
    artist = CharField(max_length=64)
    album = CharField(max_length=64)

    def __str__(self):
        return self.title


class User(AbstractUser):
    """
    User Model. Django User Model is reused and extended.
    """
    songs = models.ManyToManyField(Song, blank=True)

    def add_song(self, song):
        self.songs.add(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def __str__(self):
        return self.username

