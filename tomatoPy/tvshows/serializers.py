# -*- coding: utf-8 -*-
# tomatoPy_admin
from rest_framework import serializers

from .models import TvShow

__author__ = 'Michael Bolay'

class TvShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = TvShow
