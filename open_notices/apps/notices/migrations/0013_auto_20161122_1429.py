# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0012_notice_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='data',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='notice',
            name='details',
            field=models.TextField(blank=True, help_text='You can use markdown here', null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(help_text="e.g. 'Application for alcohol licence - House of Wine' or 'Westlow Food Bank - items required'", max_length=50),
        ),
    ]
