# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postalcodes_light', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='postalcode',
            unique_together=set([('country_code', 'postal_code')]),
        ),
    ]
