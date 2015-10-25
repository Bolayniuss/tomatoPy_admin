from django.db import models

from json_field import JSONField

from accounts.models import Client


class Setting(models.Model):
    client = models.ForeignKey(Client)
    name = models.CharField(max_length=32, null=False)

    data = JSONField()


class SettingValue(models.Model):
    setting = models.ForeignKey(Setting)
    key = models.CharField(max_length=32, null=False)
    value = models.TextField()
    type = models.CharField(max_length=32, null=False)


