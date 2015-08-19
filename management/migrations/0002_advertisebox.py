# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0002_auto_20150818_2334'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertiseBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('add0', models.ForeignKey(to='service_provider.ServiceProvider', default=None, blank=True, null=True, related_name='add_box_0')),
                ('add1', models.ForeignKey(to='service_provider.ServiceProvider', default=None, blank=True, null=True, related_name='add_box_1')),
                ('add2', models.ForeignKey(to='service_provider.ServiceProvider', default=None, blank=True, null=True, related_name='add_box_2')),
                ('add3', models.ForeignKey(to='service_provider.ServiceProvider', default=None, blank=True, null=True, related_name='add_box_3')),
                ('add4', models.ForeignKey(to='service_provider.ServiceProvider', default=None, blank=True, null=True, related_name='add_box_4')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
