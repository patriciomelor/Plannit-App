# Generated by Django 3.1.1 on 2021-06-22 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status_encargado', '0002_auto_20210621_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='sent',
            field=models.BooleanField(blank=True, default=False, verbose_name='Enviado'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='plazo',
            field=models.DateField(verbose_name='Fecha Requerimiento'),
        ),
    ]
