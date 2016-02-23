# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change_requests', '0004_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approves',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rejects',
            field=models.NullBooleanField(),
        ),
    ]
