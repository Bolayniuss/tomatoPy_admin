# -*- coding: utf-8 -*-
# tomatoPy_admin

__author__ = 'Michael Bolay'

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns("",
                       url(
                           regex=r"^$",
                           view=views.TvShowListView.as_view(),
                           name="tvshow-list"
                       ),
                       )