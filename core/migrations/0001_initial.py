# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.IntegerField()),
                ('nombre', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='rubro',
            field=models.ForeignKey(to='core.Rubro'),
        ),
    ]
