# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='actiondate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='action date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='createdate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='duedate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='due date'),
        ),
    ]
