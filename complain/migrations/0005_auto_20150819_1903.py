# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0004_auto_20150819_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='answer',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='complain',
            name='state',
            field=models.CharField(choices=[('Q', 'در حال بررسی'), ('F', 'پایان یافته')], max_length=10, default='Q'),
        ),
    ]
