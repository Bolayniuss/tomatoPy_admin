# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0002_auto_20150324_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tvshow',
            old_name='clients',
            new_name='client',
        ),
    ]
