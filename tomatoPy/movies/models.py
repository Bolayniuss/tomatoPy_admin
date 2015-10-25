from django.db import models

from accounts.models import Client


class Movie(models.Model):
    """
    Model for movie.

    title
    year
    version
    magnet_link
    """

    title = models.CharField(max_length=128)
    year = models.CharField(max_length=4)
    version = models.CharField(max_length=2, choices=(('VO', 'VO'), ('VF', 'VF')))
    magnet_link = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.title, self.year)

    def __unicode__(self):
        return u"{} ({})".format(self.title, self.year)


class MovieRegistration(models.Model):
    """
    Link model between Client and Movie

    movie
    client
    synchronized: client has already grab the movie
    """

    movie = models.ForeignKey(Movie)
    client = models.ForeignKey(Client)
    synchronized = models.BooleanField(default=False, null=False)

    def __str__(self):
        return "{} ({})".format(self.movie.title, self.movie.year)

    def __unicode__(self):
        return u"{} ({})".format(self.movie.title, self.movie.year)