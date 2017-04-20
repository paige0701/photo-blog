# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('photoblog', '0006_auto_20170420_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_confirm',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.SlugField(default=uuid.UUID('339fc65c-a63b-42c4-a987-7571f290d69d'), unique=True),
        ),
    ]
