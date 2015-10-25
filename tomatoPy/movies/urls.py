# -*- coding: utf-8 -*-
# tomatoPy_admin

__author__ = 'Michael Bolay'

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns("",
                       url(
                           regex=r"^$",
                           view=views.MovieAPIListView.as_view(),
                           name="movie-api-list"
                       ),
                       )