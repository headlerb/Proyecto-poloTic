# Generated by Django 3.1.3 on 2020-12-01 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optomedik', '0019_perfil_tipo_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='tipo_perfil',
        ),
    ]
