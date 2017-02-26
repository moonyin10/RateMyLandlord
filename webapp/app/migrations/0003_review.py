# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-26 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170226_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('reviewer_email', models.CharField(max_length=100)),
                ('review_text', models.CharField(max_length=1000)),
                ('star_rating', models.FloatField()),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Landlord')),
            ],
        ),
    ]
