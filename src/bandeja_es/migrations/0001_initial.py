# Generated by Django 3.1.1 on 2020-12-08 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('panel_carga', '0006_auto_20201118_2243'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BorradorDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_respuesta', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de respuesta')),
                ('asunto', models.CharField(max_length=50, verbose_name='Asunto')),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripcion')),
                ('status', models.BooleanField(blank=True, default=0, verbose_name='Status')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrevPaquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('prev_fecha_respuesta', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de respuesta')),
                ('prev_asunto', models.CharField(max_length=50, verbose_name='Asunto')),
                ('prev_descripcion', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripcion')),
                ('prev_status', models.BooleanField(blank=True, default=0, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Version')),
                ('comentario', models.FileField(blank=True, upload_to='proyecto/comentarios/')),
                ('archivo', models.FileField(blank=True, upload_to='proyecto/documentos/')),
                ('revision', models.CharField(default='B', max_length=1, verbose_name='Revision')),
                ('estado_cliente', models.IntegerField(blank=True, choices=[(1, 'Aprobado con Comentarios'), (2, 'Rechazado'), (3, 'Eliminado'), (4, 'Aprobado'), (5, 'Valido para construcción'), (6, 'Aprobado (en numeracion)')], default=1)),
                ('estado_contratista', models.IntegerField(blank=True, choices=[(1, 'Para revisión'), (2, 'Para aprobación')], default=1)),
                ('valido', models.BooleanField(default=1, verbose_name='Valido')),
                ('documento_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel_carga.documento')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
            ],
        ),
        migrations.CreateModel(
            name='PrevVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Version')),
                ('prev_comentario', models.FileField(blank=True, upload_to='proyecto/comentarios/')),
                ('prev_archivo', models.FileField(blank=True, upload_to='proyecto/documentos/')),
                ('prev_revision', models.CharField(default='B', max_length=1, verbose_name='Emicion/Revision')),
                ('prev_estado_cliente', models.IntegerField(blank=True, choices=[(1, 'Aprobado con Comentarios'), (2, 'Rechazado'), (3, 'Eliminado'), (4, 'Aprobado'), (5, 'Valido para construcción'), (6, 'Aprobado (en numeracion)')], default=1)),
                ('prev_estado_contratista', models.IntegerField(blank=True, choices=[(1, 'Para revisión'), (2, 'Para aprobación')], default=1)),
                ('prev_valido', models.BooleanField(default=1, verbose_name='Valido')),
                ('prev_documento_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel_carga.documento')),
                ('prev_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
            ],
        ),
        migrations.CreateModel(
            name='PrevPaqueteDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('prev_paquete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandeja_es.prevpaquete')),
                ('prev_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandeja_es.prevversion')),
            ],
        ),
        migrations.AddField(
            model_name='prevpaquete',
            name='prev_documento',
            field=models.ManyToManyField(through='bandeja_es.PrevPaqueteDocumento', to='bandeja_es.PrevVersion'),
        ),
        migrations.AddField(
            model_name='prevpaquete',
            name='prev_propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prevpropietario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prevpaquete',
            name='prev_receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prevdestinatario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PaqueteDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('paquete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandeja_es.paquete')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandeja_es.version')),
            ],
        ),
        migrations.AddField(
            model_name='paquete',
            name='version',
            field=models.ManyToManyField(through='bandeja_es.PaqueteDocumento', to='bandeja_es.Version'),
        ),
        migrations.CreateModel(
            name='BorradorVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha Version')),
                ('comentario', models.FileField(blank=True, null=True, upload_to='proyecto/comentarios/')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='proyecto/documentos/')),
                ('revision', models.CharField(blank=True, default='B', max_length=1, null=True, verbose_name='Revision')),
                ('estado_cliente', models.IntegerField(blank=True, choices=[(1, 'Aprobado con Comentarios'), (2, 'Rechazado'), (3, 'Eliminado'), (4, 'Aprobado'), (5, 'Valido para construcción'), (6, 'Aprobado (en numeracion)')], default=1, null=True)),
                ('estado_contratista', models.IntegerField(blank=True, choices=[(1, 'Para revisión'), (2, 'Para aprobación')], default=1, null=True)),
                ('documento_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel_carga.documento')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
            ],
        ),
        migrations.CreateModel(
            name='BorradorPaquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creacion')),
                ('asunto', models.CharField(blank=True, max_length=50, null=True, verbose_name='Asunto')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario_borrador', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario_borrador', to=settings.AUTH_USER_MODEL)),
                ('version', models.ManyToManyField(through='bandeja_es.BorradorDocumento', to='bandeja_es.BorradorVersion')),
            ],
        ),
        migrations.AddField(
            model_name='borradordocumento',
            name='borrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandeja_es.borradorpaquete'),
        ),
        migrations.AddField(
            model_name='borradordocumento',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandeja_es.borradorversion'),
        ),
    ]
