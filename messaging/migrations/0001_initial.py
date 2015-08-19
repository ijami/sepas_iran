# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(related_name='received_messages', to='base.SiteUser')),
                ('sender', models.ForeignKey(related_name='sent_messages', to='base.SiteUser')),
            ],
        ),
    ]
