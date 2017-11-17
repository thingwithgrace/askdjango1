# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-12 08:51
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171112_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]