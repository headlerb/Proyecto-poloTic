# Generated by Django 3.1.3 on 2020-12-03 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optomedik', '0032_pedido_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='valor_total',
        ),
    ]
