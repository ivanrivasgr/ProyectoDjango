# Generated by Django 4.1.3 on 2023-01-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_inventario_rrhh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compras',
            old_name='ano',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ano',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='taller',
            name='ano',
            field=models.IntegerField(),
        ),
    ]
