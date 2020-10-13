# Generated by Django 3.1.1 on 2020-10-13 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel_carga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='ultima_edicion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel_carga.historial'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateField(blank=True, editable=False, verbose_name='Fecha ultima edicion'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
