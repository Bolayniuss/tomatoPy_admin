# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150324_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(related_name='auth_token', to='accounts.Client')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
