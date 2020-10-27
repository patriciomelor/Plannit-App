# Generated by Django 3.1.1 on 2020-10-27 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel_carga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del paquete')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_respuesta', models.DateField(blank=True, null=True, verbose_name='Fecha de respuesta')),
                ('asunto', models.CharField(max_length=50, verbose_name='Asunto')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('periodo', models.CharField(max_length=20, verbose_name='Periodo')),
                ('status', models.CharField(default='to open', max_length=10, verbose_name='Status')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaqueteDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
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
    ]
