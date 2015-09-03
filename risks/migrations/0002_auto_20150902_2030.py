# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='code',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='risk',
            name='duration',
            field=models.CharField(max_length=40),
        ),
    ]
