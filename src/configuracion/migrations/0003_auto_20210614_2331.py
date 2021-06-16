# Generated by Django 3.1.1 on 2021-06-15 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_perfil_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='CausasNoCumplimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
            ],
        ),
        migrations.CreateModel(
            name='Restricciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
            ],
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rol_usuario',
            field=models.IntegerField(choices=[(1, 'Administrador Cliente'), (2, 'Revisor Cliente'), (3, 'Vizualizador Cliente'), (4, 'Administrador Contratista'), (5, 'Revisor Contratista'), (6, 'Vizualizador Contratista')], verbose_name='Rol de Usuario'),
        ),
    ]
