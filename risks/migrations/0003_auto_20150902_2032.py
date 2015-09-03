# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0002_auto_20150902_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='risk',
            name='duration',
            field=models.IntegerField(default=15),
        ),
    ]
