# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('siteuser_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='base.SiteUser', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=200)),
                ('long_description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.siteuser',),
        ),
        migrations.CreateModel(
            name='AirLine',
            fields=[
                ('serviceprovider_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='service_provider.ServiceProvider', serialize=False, primary_key=True)),
                ('is_international', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
            bases=('service_provider.serviceprovider',),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('serviceprovider_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='service_provider.ServiceProvider', serialize=False, primary_key=True)),
                ('degree', models.IntegerField()),
                ('has_restaurant', models.BooleanField(default=False)),
                ('has_parking', models.BooleanField(default=False)),
                ('has_internet', models.BooleanField(default=False)),
                ('has_pool', models.BooleanField(default=False)),
                ('has_conference_hall', models.BooleanField(default=False)),
                ('has_fire_extinguisher', models.BooleanField(default=False)),
                ('has_sport_salloon', models.BooleanField(default=False)),
                ('has_health_center', models.BooleanField(default=False)),
                ('has_coffeeshop', models.BooleanField(default=False)),
                ('has_emergency', models.BooleanField(default=False)),
                ('has_jungle', models.BooleanField(default=False)),
                ('has_protection_system', models.BooleanField(default=False)),
                ('has_shop_center', models.BooleanField(default=False)),
                ('has_gamenet', models.BooleanField(default=False)),
                ('has_photo_studio', models.BooleanField(default=False)),
                ('map_widget', models.CharField(null=True, blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('service_provider.serviceprovider',),
        ),
        migrations.CreateModel(
            name='TravelAgency',
            fields=[
                ('serviceprovider_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='service_provider.ServiceProvider', serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('service_provider.serviceprovider',),
        ),
    ]
