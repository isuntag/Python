# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-20 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='desc',
        ),
        migrations.AddField(
            model_name='description',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='course_app.Course'),
        ),
    ]
