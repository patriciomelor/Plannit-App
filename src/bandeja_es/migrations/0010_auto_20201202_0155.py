# Generated by Django 3.1.1 on 2020-12-02 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_carga', '0006_auto_20201118_2243'),
        ('bandeja_es', '0009_auto_20201130_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrador',
            name='documento',
            field=models.ManyToManyField(through='bandeja_es.BorradorDocumento', to='panel_carga.Documento'),
        ),
    ]
