# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('poll_survey', '0002_poll_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.IntegerField(serialize=False, primary_key=True)),
                ('comment', models.TextField()),
                ('commented_date', models.DateTimeField(auto_now=True)),
                ('commented_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='poll_post',
            name='posted_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='post_id',
            field=models.ForeignKey(to='poll_survey.Poll_Post'),
        ),
    ]
