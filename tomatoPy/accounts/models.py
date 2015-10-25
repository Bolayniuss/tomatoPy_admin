import binascii
import os

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class Client(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.TextField(default="")
    last_update = models.DateTimeField(auto_now=True)
    last_read = models.DateTimeField()

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)
        try:
            ClientToken.objects.get(user=self)
        except ObjectDoesNotExist:
            ClientToken.objects.create(user=self)

    def __str__(self):
        return "{}".format(self.name)

    def __unicode__(self):
        return u"{}".format(self.name)


@python_2_unicode_compatible
class ClientToken(models.Model):
    key = models.CharField(max_length=32)
    user = models.OneToOneField(Client, related_name='auth_token')
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(ClientToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(32)).decode()

    def __str__(self):
        return self.key