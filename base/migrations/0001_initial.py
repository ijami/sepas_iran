# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('map_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CityCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('address', models.TextField()),
                ('city', models.ForeignKey(related_name='locations', to='base.City')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(null=True, blank=True, upload_to='base/profile_images/')),
                ('telephone', models.CharField(max_length=20)),
                ('location', models.ForeignKey(to='base.Location', related_name='location_owner', null=True, blank=True)),
                ('polymorphic_ctype', models.ForeignKey(to='contenttypes.ContentType', related_name='polymorphic_base.siteuser_set+', null=True, editable=False)),
                ('primary_user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='site_user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='collection',
            field=models.ForeignKey(to='base.CityCollection', null=True, blank=True),
        ),
    ]
