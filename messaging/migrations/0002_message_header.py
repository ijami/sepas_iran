# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='header',
            field=models.CharField(default='سلام', max_length=100),
        ),
    ]
