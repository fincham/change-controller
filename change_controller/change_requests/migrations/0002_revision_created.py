# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('change_requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 2, 50, 44, 138950, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
