# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SOS_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('number1', models.IntegerField()),
                ('number2', models.IntegerField()),
                ('number3', models.IntegerField()),
            ],
        ),
    ]
