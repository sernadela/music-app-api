# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.musicapp.serializers import UserSerializer, SongSerializer
from music.musicapp.models import User, Song
from rest_framework.parsers import JSONParser
import sys, traceback
from django.db.models.base import ObjectDoesNotExist
from django.core import serializers
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class FavSongView(APIView):
    """
    API endpoint to manage user favorite songs.
    """

    parser_classes = (JSONParser,)

    def get(self, request, user, format=None):
        try:
            user = User.objects.get(id=user)
            print list(user.songs.all())
            data = serializers.serialize('json', list(user.songs.all()))
            return Response(json.loads(data), status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            traceback.print_exc(file=sys.stdout)
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, user, format=None):
        content = request.data
        try:
            user = User.objects.get(id=user)
            song = Song.objects.get(id=content['id'])
            user.add_song(song)
        except ObjectDoesNotExist:
            traceback.print_exc(file=sys.stdout)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, user, song, format=None):
        try:
            user = User.objects.get(id=user)
            song_rm = Song.objects.get(id=song)
            user.remove_song(song_rm)
        except ObjectDoesNotExist:
            traceback.print_exc(file=sys.stdout)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

