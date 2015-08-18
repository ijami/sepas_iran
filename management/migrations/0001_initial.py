# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('siteuser_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='base.SiteUser', serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.siteuser',),
        ),
    ]
