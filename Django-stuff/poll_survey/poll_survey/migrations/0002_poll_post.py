# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('poll_survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll_Post',
            fields=[
                ('poll_id', models.IntegerField(serialize=False, primary_key=True)),
                ('poll_post', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('slug_post', models.SlugField(unique=True, max_length=100)),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
