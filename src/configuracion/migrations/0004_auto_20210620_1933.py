# Generated by Django 3.1.1 on 2021-06-20 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel_carga', '0007_auto_20210526_1529'),
        ('configuracion', '0003_auto_20210614_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='causasnocumplimiento',
            name='proyecto',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='proyect_no_complete', to='panel_carga.proyecto', verbose_name='Proyecto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restricciones',
            name='proyecto',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='proyect_restrictions', to='panel_carga.proyecto', verbose_name='Proyecto'),
            preserve_default=False,
        ),
    ]
