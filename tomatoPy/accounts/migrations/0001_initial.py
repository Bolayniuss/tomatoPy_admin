# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pass_phrase', models.TextField()),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default=b'')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_read', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
