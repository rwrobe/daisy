# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0006_auto_20150903_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='risk',
            name='rating',
        ),
    ]
