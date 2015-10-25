# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_clienttoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='TvShow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('search_options', models.CharField(default=b'', max_length=128)),
                ('size_min', models.PositiveIntegerField(null=True)),
                ('size_max', models.PositiveIntegerField(null=True)),
                ('author', models.CharField(max_length=64, null=True)),
                ('title_raw_query', models.CharField(max_length=128, null=True)),
                ('starting_episode', models.CharField(max_length=8, null=True)),
                ('stopping_episode', models.CharField(max_length=8, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TvShowRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.ForeignKey(to='accounts.Client')),
                ('tvshow', models.ForeignKey(to='tvshows.TvShow')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
