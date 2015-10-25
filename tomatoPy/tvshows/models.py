from django.db import models

from accounts.models import Client


class TvShow(models.Model):
    """
    Model for tvshow.

    title
    search_options
    size_min
    size_max
    author
    title_raw_query
    starting_episode
    stopping_episode
    """

    title = models.CharField(max_length=128)
    search_filter = models.CharField(max_length=128, default="", null=False, blank=True)
    size_min = models.PositiveIntegerField(null=True, blank=True)
    size_max = models.PositiveIntegerField(null=True, blank=True)
    author_filter = models.CharField(max_length=64, null=True, blank=True)
    title_raw_query = models.CharField(max_length=128, null=True, blank=True)
    starting_episode = models.SmallIntegerField(null=False, blank=False, default=0)
    starting_season = models.SmallIntegerField(null=False, blank=False, default=0)
    stopping_episode = models.SmallIntegerField(null=True, blank=True)
    stopping_season = models.SmallIntegerField(null=True, blank=True)
    client = models.ManyToManyField(Client)

    def __str__(self):
        return "{}".format(self.title)

    def __unicode__(self):
        return u"{}".format(self.title)
