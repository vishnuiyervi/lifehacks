# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='end',
            field=models.DateTimeField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tip',
            name='start',
            field=models.DateTimeField(max_length=50),
        ),
    ]