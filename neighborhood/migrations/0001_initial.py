# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 11:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood_name', models.CharField(max_length=50)),
                ('neighborhood_location', models.CharField(max_length=50, null=True)),
                ('occupants', models.IntegerField(null=True)),
                ('health_dept', models.IntegerField(default='999')),
                ('police_dept', models.IntegerField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]