# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_clienttoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clienttoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClientToken',
        ),
    ]
