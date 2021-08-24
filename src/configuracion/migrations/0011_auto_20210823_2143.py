# Generated by Django 3.1.1 on 2021-08-24 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0010_auto_20210818_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historialumbrales',
            name='tiempo_control',
        ),
        migrations.RemoveField(
            model_name='historialumbrales',
            name='variable_atraso',
        ),
        migrations.AddField(
            model_name='historialumbrales',
            name='cliente_tiempo_control',
            field=models.IntegerField(default=0, verbose_name='Cliente Días de notificación'),
        ),
        migrations.AddField(
            model_name='historialumbrales',
            name='cliente_variable_atraso',
            field=models.IntegerField(default=0, verbose_name='Cliente Días de atraso'),
        ),
        migrations.AddField(
            model_name='historialumbrales',
            name='contratista_tiempo_control',
            field=models.IntegerField(default=0, verbose_name='Contratista Días de notificación'),
        ),
        migrations.AddField(
            model_name='historialumbrales',
            name='contratista_variable_atraso',
            field=models.IntegerField(default=0, verbose_name='Contratista Días de atraso'),
        ),
    ]
