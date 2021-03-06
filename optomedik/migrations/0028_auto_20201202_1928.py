# Generated by Django 3.1.3 on 2020-12-03 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('optomedik', '0027_auto_20201202_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'verbose_name': 'registrop', 'verbose_name_plural': 'optomedik'},
        ),
        migrations.AlterModelOptions(
            name='turnos',
            options={'verbose_name': 'registro', 'verbose_name_plural': 'optomedik'},
        ),
        migrations.AddField(
            model_name='paciente',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
