# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-21 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20170221_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='type',
            field=models.CharField(choices=[('фірмові_страви', 'фірмові_страви'), ('салат', 'салат'), ('холодні_закуски', 'холодні_закуски'), ('гарячі_закуски', 'гарячі_закуски'), ('перші_страви', 'перші_страви'), ('другі_страви', 'другі_страви'), ('гарніри', 'гарніри'), ('чай', 'чай'), ('кава', 'кава')], max_length=30),
        ),
    ]