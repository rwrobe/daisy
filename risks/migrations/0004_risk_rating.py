# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0003_auto_20150902_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
