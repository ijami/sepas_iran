# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('service_provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('address', models.TextField()),
                ('city', models.ForeignKey(related_name='airports', to='base.City')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('send_time', models.DateTimeField(auto_now=True)),
                ('sender', models.ForeignKey(related_name='comments', to='base.SiteUser')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('price', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('sold_number', models.CharField(max_length=20)),
                ('tag_line', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, blank=True, upload_to='base/service_images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='service.Service', serialize=False, primary_key=True)),
                ('flight_number', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('airplane', models.CharField(max_length=40)),
                ('airline', models.ForeignKey(related_name='flights', to='service_provider.AirLine')),
                ('destination', models.ForeignKey(related_name='flight_arrivals', to='base.City')),
                ('origin', models.ForeignKey(related_name='flight_departures', to='base.City')),
            ],
            options={
                'abstract': False,
            },
            bases=('service.service',),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='service.Service', serialize=False, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('number_of_bed', models.IntegerField()),
                ('has_television', models.BooleanField(default=False)),
                ('has_telephone', models.BooleanField(default=False)),
                ('has_bathroom', models.BooleanField(default=False)),
                ('hotel', models.ForeignKey(related_name='rooms', to='service_provider.Hotel')),
            ],
            options={
                'abstract': False,
            },
            bases=('service.service',),
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='service.Service', serialize=False, primary_key=True)),
                ('going_date', models.DateField()),
                ('return_date', models.DateField()),
                ('description', models.TextField()),
                ('hotel_name', models.CharField(null=True, blank=True, max_length=100)),
                ('tour_guide_name', models.CharField(max_length=100)),
                ('destination', models.ForeignKey(related_name='arrivals', to='base.City')),
                ('origin', models.ForeignKey(related_name='departures', to='base.City')),
                ('travel_agency', models.ForeignKey(related_name='tours', to='service_provider.TravelAgency')),
            ],
            options={
                'abstract': False,
            },
            bases=('service.service',),
        ),
        migrations.AddField(
            model_name='service',
            name='polymorphic_ctype',
            field=models.ForeignKey(to='contenttypes.ContentType', related_name='polymorphic_service.service_set+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='service',
            field=models.ForeignKey(related_name='comments', to='service.Service'),
        ),
    ]
