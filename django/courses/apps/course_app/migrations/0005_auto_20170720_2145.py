# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-20 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_auto_20170720_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='course_app.Course'),
        ),
    ]
