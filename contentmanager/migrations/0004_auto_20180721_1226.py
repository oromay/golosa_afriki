# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-21 17:26
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentmanager', '0003_auto_20171217_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=ckeditor.fields.RichTextField(verbose_name='Короткая справка'),
        ),
        migrations.AlterField(
            model_name='new',
            name='content',
            field=models.TextField(),
        ),
    ]
