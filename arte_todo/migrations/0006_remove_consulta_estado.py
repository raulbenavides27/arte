# Generated by Django 4.0.5 on 2022-06-27 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arte_todo', '0005_rename_contacto_consulta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='estado',
        ),
    ]
