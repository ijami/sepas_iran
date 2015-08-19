# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0002_auto_20150818_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovider',
            name='pic',
            field=models.ImageField(upload_to='images', default=1),
            preserve_default=False,
        ),
    ]
