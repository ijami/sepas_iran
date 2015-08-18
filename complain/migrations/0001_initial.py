# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(choices=[('Q', 'در صف بررسی'), ('H', 'در حال بررسی'), ('S', 'صدور حکم'), ('F', 'پایان یافته')], default='Q', max_length=10)),
                ('last_state_change', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.IntegerField()),
                ('price_state', models.CharField(choices=[('G', 'مناسب'), ('E', 'گران'), ('C', 'ارزان')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FlightPoll',
            fields=[
                ('poll_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='complain.Poll', serialize=False, primary_key=True)),
                ('was_on_time', models.BooleanField()),
                ('workers_rate', models.IntegerField()),
                ('pilot_rate', models.IntegerField()),
            ],
            bases=('complain.poll',),
        ),
        migrations.CreateModel(
            name='RoomPoll',
            fields=[
                ('poll_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='complain.Poll', serialize=False, primary_key=True)),
                ('food_rate', models.IntegerField()),
                ('workers_rate', models.IntegerField()),
                ('cleanliness_rate', models.IntegerField()),
            ],
            bases=('complain.poll',),
        ),
        migrations.CreateModel(
            name='TourPoll',
            fields=[
                ('poll_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='complain.Poll', serialize=False, primary_key=True)),
                ('guide_rate', models.BooleanField()),
                ('discipline_rate', models.IntegerField()),
                ('hotel_rate', models.IntegerField()),
                ('flight_rate', models.IntegerField()),
            ],
            bases=('complain.poll',),
        ),
    ]
