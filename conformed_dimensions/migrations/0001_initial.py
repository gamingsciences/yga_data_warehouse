# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-26 12:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateDimension',
            fields=[
                ('datekey', models.IntegerField(primary_key=True, serialize=False)),
                ('full_date', models.DateField()),
                ('day_of_week', models.IntegerField()),
                ('day_num_in_month', models.IntegerField()),
                ('day_name', models.CharField(max_length=9)),
                ('day_abbrev', models.CharField(max_length=3)),
                ('weekday_flag', models.BooleanField()),
                ('week_num_in_year', models.IntegerField()),
                ('week_begin_date', models.DateField()),
                ('week_begin_datekey', models.IntegerField()),
                ('month', models.IntegerField()),
                ('month_name', models.CharField(max_length=9)),
                ('month_abbrev', models.CharField(max_length=3)),
                ('quarter', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('yearmo', models.IntegerField()),
                ('month_end_flag', models.BooleanField()),
                ('holiday_flag', models.BooleanField()),
            ],
            options={
                'db_table': 'date_dim',
            },
        ),
        migrations.CreateModel(
            name='EmployeeDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(unique=True)),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'employee_dim',
            },
        ),
        migrations.CreateModel(
            name='LocationDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casino', models.CharField(max_length=50, null=True)),
                ('area', models.CharField(max_length=5, null=True)),
                ('section', models.CharField(max_length=5, null=True)),
                ('position', models.CharField(max_length=5, null=True)),
                ('location', models.CharField(max_length=20, null=True)),
                ('bank_type', models.CharField(max_length=20, null=True)),
                ('position_type', models.CharField(max_length=20, null=True)),
                ('non_smoking_flag', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'location_dim',
            },
        ),
        migrations.CreateModel(
            name='PitGameDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_type', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'pitgame_dim',
            },
        ),
        migrations.CreateModel(
            name='PitGameRevenueDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oasis_id', models.IntegerField()),
                ('game', models.CharField(max_length=50)),
                ('game_type', models.CharField(max_length=50)),
                ('pit', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'pitgame_revenue_dim',
            },
        ),
        migrations.CreateModel(
            name='PlayerDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField()),
                ('effective_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 0, 0))),
                ('current', models.BooleanField(default=False)),
                ('date_joined', models.DateField()),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('gender', models.CharField(max_length=5, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('address_a', models.CharField(max_length=50, null=True)),
                ('address_b', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('city_state', models.CharField(max_length=50, null=True)),
                ('zip_code', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('call_flag', models.BooleanField(default=False)),
                ('mail_flag', models.BooleanField(default=False)),
                ('distance', models.IntegerField(null=True)),
                ('addr_lat', models.FloatField(null=True)),
                ('addr_lon', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'player_dim',
            },
        ),
        migrations.CreateModel(
            name='ShiftDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(blank=True, max_length=20, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'shift_dim',
            },
        ),
        migrations.CreateModel(
            name='SlotGameDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.IntegerField()),
                ('effective_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 0, 0))),
                ('current', models.BooleanField(default=False)),
                ('game_type', models.CharField(max_length=50, null=True)),
                ('denomination', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(max_length=50, null=True)),
                ('cabinet', models.CharField(max_length=50, null=True)),
                ('par', models.FloatField(null=True)),
                ('num_reels', models.IntegerField(null=True)),
                ('num_coins', models.IntegerField(null=True)),
                ('num_paylines', models.IntegerField(null=True)),
                ('volatility', models.FloatField(blank=True, null=True)),
                ('progressive', models.BooleanField(default=False)),
                ('manufacturer', models.CharField(max_length=50, null=True)),
                ('multigame', models.BooleanField(default=False)),
                ('multidenom', models.BooleanField(default=False)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'db_table': 'slotgame_dim',
            },
        ),
        migrations.CreateModel(
            name='TimeDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minute_of_day', models.IntegerField(default=0)),
                ('hour', models.IntegerField(default=0)),
                ('minute', models.IntegerField(default=0)),
                ('clock_time', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'time_dim',
            },
        ),
        migrations.AlterUniqueTogether(
            name='playerdimension',
            unique_together=set([('player_id', 'effective_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='locationdimension',
            unique_together=set([('casino', 'area', 'section', 'position')]),
        ),
        migrations.AlterUniqueTogether(
            name='slotgamedimension',
            unique_together=set([('slot_number', 'effective_date')]),
        ),
    ]
