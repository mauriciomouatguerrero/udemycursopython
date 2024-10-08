# Generated by Django 5.1.1 on 2024-09-14 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['id'], 'verbose_name': 'Departamentos', 'verbose_name_plural': 'Areas de la Empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'short_name')},
        ),
    ]
