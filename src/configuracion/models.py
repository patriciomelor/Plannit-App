from bandeja_es.models import Version
from notifications.models import Notificacion
from panel_carga.models import Documento, Proyecto
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.contrib.postgres.fields import ArrayField

from .roles import *

def get_full_name(self):
    return str(self.first_name+" "+self.last_name)

User.add_to_class("__str__", get_full_name)
User._meta.get_field('email')._unique = True

class Perfil(models.Model):
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    foto_de_perfil = models.ImageField(upload_to="perfil/foto/%Y/%m/%d", blank=True, null=True )
    rol_usuario = models.IntegerField(verbose_name='Rol de Usuario', choices=ROLES)
    empresa = models.CharField(verbose_name='Empresa', max_length=64, default="")
    cargo_empresa = models.CharField(verbose_name='Cargo en Empresa', max_length=128, default="")
    client = models.BooleanField(verbose_name='Es cliente', default=True)

    def __str__(self):
        return str(self.get_rol_usuario_display())
        

class Restricciones(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=30)
    created_at = models.DateTimeField(verbose_name="Fecha Creación", auto_now_add=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyect_restrictions", verbose_name="Proyecto")
    def __str__(self):
        return self.nombre

class CausasNoCumplimiento(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=30)
    created_at = models.DateTimeField(verbose_name="Fecha Creación", auto_now_add=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyect_no_complete", verbose_name="Proyecto")

    def __str__(self):
        return self.nombre

class Umbral(models.Model):
    """
    4 umbrales inmodificables
    """
    nombre = models.CharField(max_length=100, editable=False, default="")
    descripcion =  models.CharField(max_length=256, editable=False, default="")


class HistorialUmbrales(models.Model):
    umbral = models.ForeignKey(Umbral, on_delete=models.CASCADE, related_name="umbral")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="hu_proyecto")
    cliente_tiempo_control = models.IntegerField(verbose_name="Cliente Días de notificación", default=0, blank=True, null=True)
    cliente_variable_atraso = models.IntegerField(verbose_name="Cliente Días de atraso", default=0, blank=True, null=True)
    contratista_tiempo_control = models.IntegerField(verbose_name="Contratista Días de notificación", default=0, blank=True, null=True)
    contratista_variable_atraso = models.IntegerField(verbose_name="Contratista Días de atraso", default=0, blank=True, null=True)
    last_checked = models.DateTimeField(verbose_name="Ultima Revisión")

class NotificacionHU(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    h_umbral = models.ForeignKey(HistorialUmbrales, on_delete=models.CASCADE, related_name="historial_umbral")
    notificacion = models.OneToOneField(Notificacion, on_delete=models.CASCADE, related_name="hu_notificacion")
    documentos = models.ManyToManyField(Documento, related_name="hu_documentos", verbose_name="Listado de Documentos")
    versiones = models.ManyToManyField(Version, related_name="hu_versiones", verbose_name="Listado de Versiones")
    porcentaje_atraso = ArrayField(null=True, base_field=models.FloatField(verbose_name="porcentaje de atraso", blank=True, null=True))
    #[Avance Real, Avance Programado, Desviación %]