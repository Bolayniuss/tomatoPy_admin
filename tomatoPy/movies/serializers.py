# -*- coding: utf-8 -*-
# tomatoPy_admin
from rest_framework import serializers
from .models import MovieRegistration, Movie

__author__ = 'Michael Bolay'


class MovieSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Movie
