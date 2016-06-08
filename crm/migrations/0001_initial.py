# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 15:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Changes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=10)),
                ('orig_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('phone_main', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('do_not_email', models.BooleanField(default=False)),
                ('do_not_call', models.BooleanField(default=False)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('dept', models.CharField(blank=True, max_length=50)),
                ('industry', models.TextField(blank=True)),
                ('geo', models.CharField(blank=True, max_length=10)),
                ('main_category', models.CharField(blank=True, max_length=25)),
                ('main_category2', models.CharField(blank=True, max_length=15)),
                ('division1', models.CharField(blank=True, max_length=20)),
                ('division2', models.CharField(blank=True, max_length=20)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_modified', models.DateTimeField(verbose_name='date modified')),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orig_person_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orig_person_modifed_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_contact', models.DateTimeField(verbose_name='date of contact')),
                ('notes', models.TextField()),
                ('method', models.CharField(choices=[('Pitch', 'Sales Pitch (Phone)'), ('Followup', 'Follow-up Call'), ('Email', 'Follow-up Email'), ('Marketing', 'Marketing Email'), ('Registration', 'Delegate registration'), ('Speaker', 'Speaker confirmation'), ('Sponsor', 'Sponsor booking'), ('Research', 'PD Research Call')], default='Pitch', max_length=20)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_pk', models.IntegerField()),
                ('original_person_id', models.IntegerField()),
                ('date_of_contact', models.DateTimeField(verbose_name='date of contact')),
                ('notes', models.TextField()),
                ('method', models.CharField(max_length=20)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('date_begins', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ListSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo', models.CharField(blank=True, choices=[('East', 'East'), ('West', 'West'), ('Maritimes/East', 'Maritimes'), ('USA', 'USA'), ('Other', 'Other Foreign'), ('Unknown', 'Unknown'), ('', '---')], default='', max_length=10)),
                ('main_category', models.CharField(blank=True, choices=[('HR', 'HR'), ('FIN', 'FIN'), ('Industry', 'Industry'), ('Aboriginal', 'Aboriginal'), ('Gov', 'Gov'), ('NA', 'None'), ('', '---')], default='', max_length=25)),
                ('main_category2', models.CharField(blank=True, choices=[('HR', 'HR'), ('FIN', 'FIN'), ('Industry', 'Industry'), ('Aboriginal', 'Aboriginal'), ('Gov', 'Gov'), ('NA', 'None'), ('', '---')], default='', max_length=15)),
                ('division1', models.CharField(blank=True, choices=[('1', '1 - Misc'), ('2', '2 - Misc'), ('3', '3 - Misc'), ('4', '4 - Misc'), ('5', '5 - Misc'), ('6', '6 - Misc'), ('A1', '1 - Accounting'), ('A2', '2 - Accounting'), ('A3', '3 - Accounting'), ('Aboriginal', 'Aboriginal'), ('FED 1', 'FED 1'), ('FED 2', 'FED 2'), ('FED 3', 'FED 3'), ('FED 4', 'FED 4'), ('USA', 'USA'), ('NA', 'Not Determined'), ('', '---')], default='', max_length=20)),
                ('division2', models.CharField(blank=True, choices=[('1', '1 - Misc'), ('2', '2 - Misc'), ('3', '3 - Misc'), ('4', '4 - Misc'), ('5', '5 - Misc'), ('6', '6 - Misc'), ('A1', '1 - Accounting'), ('A2', '2 - Accounting'), ('A3', '3 - Accounting'), ('Aboriginal', 'Aboriginal'), ('FED 1', 'FED 1'), ('FED 2', 'FED 2'), ('FED 3', 'FED 3'), ('FED 4', 'FED 4'), ('USA', 'USA'), ('NA', 'Not Determined'), ('', '---')], default='', max_length=20)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('industry', models.CharField(blank=True, max_length=100)),
                ('include_exclude', models.CharField(choices=[('include', 'include'), ('exclude', 'exclude')], default='include', max_length=7)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('phone_main', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('do_not_email', models.BooleanField(default=False)),
                ('do_not_call', models.BooleanField(default=False)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('dept', models.CharField(blank=True, max_length=50)),
                ('industry', models.TextField(blank=True)),
                ('geo', models.CharField(choices=[('East', 'East'), ('West', 'West'), ('Maritimes/East', 'Maritimes'), ('USA', 'USA'), ('Other', 'Other Foreign'), ('Unknown', 'Unknown')], default='Unknown', max_length=10)),
                ('main_category', models.CharField(choices=[('HR', 'HR'), ('FIN', 'FIN'), ('Industry', 'Industry'), ('Aboriginal', 'Aboriginal'), ('Gov', 'Gov'), ('NA', 'None')], default='Industry', max_length=25)),
                ('main_category2', models.CharField(choices=[('HR', 'HR'), ('FIN', 'FIN'), ('Industry', 'Industry'), ('Aboriginal', 'Aboriginal'), ('Gov', 'Gov'), ('NA', 'None')], default='NA', max_length=15)),
                ('division1', models.CharField(choices=[('1', '1 - Misc'), ('2', '2 - Misc'), ('3', '3 - Misc'), ('4', '4 - Misc'), ('5', '5 - Misc'), ('6', '6 - Misc'), ('A1', '1 - Accounting'), ('A2', '2 - Accounting'), ('A3', '3 - Accounting'), ('Aboriginal', 'Aboriginal'), ('FED 1', 'FED 1'), ('FED 2', 'FED 2'), ('FED 3', 'FED 3'), ('FED 4', 'FED 4'), ('USA', 'USA'), ('NA', 'Not Determined')], default='NA', max_length=20)),
                ('division2', models.CharField(blank=True, choices=[('1', '1 - Misc'), ('2', '2 - Misc'), ('3', '3 - Misc'), ('4', '4 - Misc'), ('5', '5 - Misc'), ('6', '6 - Misc'), ('A1', '1 - Accounting'), ('A2', '2 - Accounting'), ('A3', '3 - Accounting'), ('Aboriginal', 'Aboriginal'), ('FED 1', 'FED 1'), ('FED 2', 'FED 2'), ('FED 3', 'FED 3'), ('FED 4', 'FED 4'), ('USA', 'USA'), ('NA', 'Not Determined')], default='NA', max_length=20)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_modified', models.DateTimeField(verbose_name='date modified')),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='person_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='person_modifed_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.CharField(blank=True, choices=[('1', 'Red'), ('2', 'Green'), ('3', 'Blue'), ('4', 'Orange'), ('5', 'Yellow'), ('6', 'Pink'), ('7', 'Pirate'), ('', '---')], default='', max_length=1)),
                ('follow_up_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Event')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Person')),
            ],
        ),
        migrations.AddField(
            model_name='listselection',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Person'),
        ),
        migrations.AddField(
            model_name='deletedcontact',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Event'),
        ),
        migrations.AddField(
            model_name='contact',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Event'),
        ),
        migrations.AddField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Person'),
        ),
    ]
