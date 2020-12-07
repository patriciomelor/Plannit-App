# Generated by Django 3.1.1 on 2020-11-26 17:29

import bandeja_es.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel_carga', '0006_auto_20201118_2243'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bandeja_es', '0007_auto_20201125_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrador',
            name='documento',
            field=models.ManyToManyField(blank=True, through='bandeja_es.BorradorDocumento', to='panel_carga.Documento'),
        ),
        migrations.CreateModel(
            name='BorradorVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Version')),
                ('comentario', models.FileField(blank=True, upload_to='proyecto/comentarios/')),
                ('archivo', models.FileField(blank=True, upload_to='proyecto/documentos/')),
                ('revision', models.CharField(default='B', max_length=1, verbose_name='Emicion/Revision')),
                ('estado_cliente', models.IntegerField(blank=True, choices=[(1, 'Aprobado con Comentarios'), (2, 'Rechazado'), (3, 'Eliminado'), (4, 'Aprobado'), (5, 'Valido para construcción'), (6, 'Aprobado (en numeracion)')], default=1)),
                ('estado_contratista', models.IntegerField(blank=True, choices=[(1, 'Para revisión'), (2, 'Para aprobación')], default=1)),
                ('documento_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel_carga.documento')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
                ('paquete_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandeja_es.paquete', verbose_name=bandeja_es.models.Paquete)),
            ],
        ),
    ]