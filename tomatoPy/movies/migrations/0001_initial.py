# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_clienttoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('year', models.CharField(max_length=4)),
                ('version', models.CharField(max_length=2, choices=[(b'VO', b'VO'), (b'VF', b'VF')])),
                ('magnet_link', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('synchronized', models.BooleanField(default=False)),
                ('client', models.ForeignKey(to='accounts.Client')),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
