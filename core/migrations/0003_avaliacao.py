# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171211_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrelas', models.PositiveIntegerField(blank=True, null=True, verbose_name='Estrelas')),
                ('nota', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota')),
                ('ocorrencias', models.TextField(blank=True, null=True, verbose_name='Ocorrências')),
                ('avaliador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Avaliador')),
                ('projeto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Projeto')),
            ],
        ),
    ]