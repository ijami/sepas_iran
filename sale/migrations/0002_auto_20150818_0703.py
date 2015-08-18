# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
        ('service', '0001_initial'),
        ('tourist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitem',
            name='service',
            field=models.ForeignKey(to='service.Service'),
        ),
        migrations.AddField(
            model_name='factor',
            name='tourist',
            field=models.ForeignKey(related_name='factors', to='tourist.Tourist'),
        ),
    ]
