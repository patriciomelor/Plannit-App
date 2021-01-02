from django.shortcuts import render
from django.urls import (reverse_lazy, reverse)
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView, View
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, FormView)
from panel_carga.views import ProyectoMixin
from bandeja_es.models import Version
from panel_carga.models import Documento

# Create your views here.


class IndexAnalitica(ProyectoMixin, TemplateView):
    template_name =  'analitica/index.html'
    ###################################################
    #                                                 #
    #                                                 #
    #   PRIMER GRÁFICO DE ESTADOS DE LOS DOCUMENTOS   #
    #                                                 #
    #                                                 #
    ###################################################
    def get_report_states_AcC(self):
        version_aprobadocCs = Version.objects.filter(estado_cliente = 1).count() #Aprobado con comentarios
        return version_aprobadocCs

    def get_report_states_Rec(self):
        version_rechazados = Version.objects.filter(estado_cliente = 2).count() #Rechazado
        return version_rechazados

    def get_report_states_Eli(self):
        version_eliminados = Version.objects.filter(estado_cliente = 3).count() #Eliminado
        return version_eliminados
        
    def get_report_states_Apr(self):
        version_aprobados = Version.objects.filter(estado_cliente = 4).count() #Aprobado
        return version_aprobados

    def get_report_states_VcC(self):
        version_validoConss = Version.objects.filter(estado_cliente = 5).count() #Valido para construcción
        return version_validoConss

    def get_report_states_ANu(self):
        version_aprobadoNums = Version.objects.filter(estado_cliente = 6).count() #Aprobado en número
        return version_aprobadoNums

    def get_report_states_total(self):
        total = Version.objects.all().count() #Total de documentos (Versiones)
        return total

    ###################################################
    #                                                 #
    #                                                 #
    #   SEGUNDO GRÁFICO DE EMITIDOS POR SUBESTACION   #
    #                                                 #
    #                                                 #
    ###################################################

    def get_report_issued_substation(self):
        especialidad = Documento.objects.filter(Especialidad).str() #especialidad mecanica


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_report_states_AcC'] = self.get_report_states_AcC()
        context['get_report_states_Rec'] = self.get_report_states_Rec()
        context['get_report_states_Eli'] = self.get_report_states_Eli()
        context['get_report_states_Apr'] = self.get_report_states_Apr()
        context['get_report_states_VcC'] = self.get_report_states_VcC()
        context['get_report_states_ANu'] = self.get_report_states_ANu()
        context['get_report_states_total'] = self.get_report_states_total()
        return context