# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_display', '0006_auto_20160416_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='camera',
            name='productIdd',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'description', 'price']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='warranty',
        ),
        migrations.DeleteModel(
            name='Camera',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product_display.Category'),
        ),
    ]
