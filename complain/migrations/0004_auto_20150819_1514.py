# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0003_complain_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='service_item',
            field=models.OneToOneField(to='sale.ServiceItem', related_name='complain'),
        ),
    ]
