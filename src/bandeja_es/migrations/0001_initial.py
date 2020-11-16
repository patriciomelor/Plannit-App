# Generated by Django 3.1.1 on 2020-11-16 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel_carga', '0004_auto_20201112_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('asunto', models.CharField(max_length=50, verbose_name='Asunto')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario_borrador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_respuesta', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de respuesta')),
                ('asunto', models.CharField(max_length=50, verbose_name='Asunto')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('status', models.BooleanField(blank=True, default=0, verbose_name='Status')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_version', models.CharField(max_length=5, verbose_name='Version documento')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Version')),
                ('comentario', models.FileField(blank=True, upload_to='proyecto/comentarios/')),
                ('archivo', models.FileField(blank=True, upload_to='proyecto/documentos/')),
                ('revision', models.CharField(default='B', max_length=1, verbose_name='Emicion/Revision')),
                ('estado_cliente', models.IntegerField(blank=True, choices=[(1, 'Aprobado con Comentarios'), (2, 'Rechazado'), (3, 'Eliminado'), (4, 'Aprobado'), (5, 'Valido para construcción'), (6, 'Aprobado (en numeracion)')], default=1)),
                ('estado_contratista', models.IntegerField(blank=True, choices=[(1, 'Para revisión'), (2, 'Para aprobación')], default=1)),
                ('documento_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel_carga.documento')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
            ],
        ),
        migrations.CreateModel(
            name='PaqueteDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('documento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel_carga.documento')),
                ('paquete_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandeja_es.paquete')),
            ],
        ),
        migrations.AddField(
            model_name='paquete',
            name='documento',
            field=models.ManyToManyField(through='bandeja_es.PaqueteDocumento', to='panel_carga.Documento'),
        ),
        migrations.AddField(
            model_name='paquete',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BorradorDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('borrador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandeja_es.borrador')),
                ('documento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel_carga.documento')),
            ],
        ),
        migrations.AddField(
            model_name='borrador',
            name='documento',
            field=models.ManyToManyField(through='bandeja_es.BorradorDocumento', to='panel_carga.Documento'),
        ),
        migrations.AddField(
            model_name='borrador',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario_borrador', to=settings.AUTH_USER_MODEL),
        ),
    ]
