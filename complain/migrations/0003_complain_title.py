# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0002_auto_20150818_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='title',
            field=models.CharField(max_length=300, default='شکایت'),
        ),
    ]
