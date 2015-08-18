# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
        ('complain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='service_item',
            field=models.ForeignKey(related_name='polls', to='sale.ServiceItem'),
        ),
        migrations.AddField(
            model_name='complain',
            name='service_item',
            field=models.ForeignKey(to='sale.ServiceItem'),
        ),
    ]
