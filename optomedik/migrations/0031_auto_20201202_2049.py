# Generated by Django 3.1.3 on 2020-12-03 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optomedik', '0030_auto_20201202_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='estado',
        ),
        migrations.DeleteModel(
            name='estado',
        ),
    ]
