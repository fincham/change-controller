# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change_requests', '0005_auto_20150603_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='revision',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='revision',
            name='number',
        ),
    ]
