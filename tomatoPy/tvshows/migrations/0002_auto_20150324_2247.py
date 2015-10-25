# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20150324_2247'),
        ('tvshows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='clients',
            field=models.ManyToManyField(to='accounts.Client'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='author',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='search_options',
            field=models.CharField(default=b'', max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='size_max',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='size_min',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='starting_episode',
            field=models.CharField(max_length=8, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='stopping_episode',
            field=models.CharField(max_length=8, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='title_raw_query',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
