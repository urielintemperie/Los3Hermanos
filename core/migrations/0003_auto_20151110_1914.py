# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pedido_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='codigoDeCompra',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='codigoDeCompra',
        ),
    ]
