# Generated by Django 3.1.3 on 2020-12-03 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optomedik', '0040_vendedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='id_vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_vendedor', to='optomedik.vendedor'),
        ),
    ]
