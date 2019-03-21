# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-12 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_modified_default_attribute_of_visible_field_to_false'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=30),
        ),
    ]
