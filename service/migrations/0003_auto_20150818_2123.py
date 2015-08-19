# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_tour_trans_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='type',
            field=models.CharField(default='Flight', max_length=10),
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.CharField(default='Room', max_length=10),
        ),
        migrations.AddField(
            model_name='tour',
            name='type',
            field=models.CharField(default='Tour', max_length=10),
        ),
    ]
