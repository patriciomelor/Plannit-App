# Generated by Django 3.1.1 on 2020-10-27 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=100, verbose_name='Especialidad')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('num_documento', models.CharField(max_length=100, unique=True, verbose_name='Codigo Documento')),
                ('tipo', models.CharField(choices=[('PLANO', 'PLANO'), ('DOCUMENTO', 'DOCUMENTO')], max_length=15, verbose_name='Tipo Documento')),
                ('archivo', models.FileField(blank=True, upload_to='proyecto/documentos/')),
                ('fecha_inicio_Emision', models.DateField(blank=True, default=None, verbose_name='Fecha inicio emisión')),
                ('fecha_fin_Emision', models.DateField(blank=True, default=None, verbose_name='Fecha inicio emisión')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'Revision B'), (2, 'Revision C'), (3, 'Revision D'), (4, 'Revision E'), (5, 'Revision F'), (6, 'Revision G'), (7, 'Revision H'), (8, 'Revision I'), (9, 'Revision J'), (10, 'Revision K'), (11, 'Revision L'), (12, 'Revision M'), (13, 'Revision N'), (14, 'Revision O'), (15, 'Revision P'), (16, 'Revision Q'), (17, 'Revision R'), (18, 'Revision S'), (19, 'Revision T'), (20, 'Revision U'), (21, 'Revision V'), (22, 'Revision W'), (23, 'Revision X'), (24, 'Revision Y'), (25, 'Revision Z'), (26, 'Revision 0'), (27, 'Revision 1'), (28, 'Revision 2'), (29, 'Revision 3'), (30, 'Revision 4'), (31, 'Revision 5'), (32, 'Revision 6'), (33, 'Revision 7'), (34, 'Revision 8'), (35, 'Revision 9')], default=1, verbose_name='Tipo Revision')),
                ('estado_cliente', models.IntegerField(choices=[(1, 'Aprobado con Comentarios'), (2, 'Rechazado'), (3, 'Eliminado'), (4, 'Aprobado'), (5, 'Valido para construcción'), (6, 'Aprobado')], default=1)),
                ('estado_contratista', models.IntegerField(choices=[(1, 'Para revisión'), (2, 'Para aprobación')], default=1)),
                ('emitida_para', models.TextField(verbose_name='Emitida para')),
                ('fecha', models.DateField(editable=False, verbose_name='Fecha')),
                ('fecha_estimada', models.DateField(default='2021-01-01', verbose_name='Fecha rev 0')),
                ('documento', models.ForeignKey(blank=True, default=5, on_delete=django.db.models.deletion.CASCADE, to='panel_carga.documento')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre del Proyecto')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de Inicio')),
                ('fecha_termino', models.DateField(blank=True, verbose_name='Fecha de Termino')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
                ('encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha ultima edicion')),
                ('documento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='panel_carga.documento')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='documento',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel_carga.proyecto'),
        ),
    ]