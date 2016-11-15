# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_description_short', models.CharField(max_length=400)),
                ('event_description_long', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('event_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Job_Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posting_name', models.CharField(max_length=200)),
                ('job_description_short', models.CharField(max_length=400)),
                ('job_description_long', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('pay', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Musician_Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musician_name', models.CharField(max_length=200)),
                ('ad_description_short', models.CharField(max_length=400)),
                ('ad_description_long', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('start_availability', models.DateTimeField()),
                ('end_availability', models.DateTimeField()),
            ],
        ),
    ]
