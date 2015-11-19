# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('costoUnidad', models.IntegerField()),
                ('codigoDeCompra', models.CharField(max_length=64)),
                ('producto', models.ForeignKey(to='core.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('costoUnidad', models.IntegerField()),
                ('codigoDeCompra', models.CharField(max_length=64)),
                ('producto', models.ForeignKey(to='core.Producto')),
            ],
        ),
    ]
