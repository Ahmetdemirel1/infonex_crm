# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_masterlistselections'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TerritorySelects',
            new_name='PersonalListSelections',
        ),
    ]
