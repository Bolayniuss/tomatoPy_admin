# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0003_auto_20150324_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshowregistration',
            name='client',
        ),
        migrations.RemoveField(
            model_name='tvshowregistration',
            name='tvshow',
        ),
        migrations.DeleteModel(
            name='TvShowRegistration',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='author',
            new_name='author_filter',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='search_options',
            new_name='search_filter',
        ),
    ]
