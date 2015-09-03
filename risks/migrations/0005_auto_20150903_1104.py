# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0004_risk_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='id',
            field=models.IntegerField(default=0, unique=True, serialize=False, primary_key=True),
        ),
    ]
