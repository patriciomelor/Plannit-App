from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import FormView, CreateView, DeleteView, UpdateView, ListView, DetailView
from panel_carga.views import ProyectoMixin
from django.contrib.auth.models import User

from .models import Perfil
from .forms import CrearUsuario, EditUsuario

# Create your views here.
class UsuarioView(ProyectoMixin, CreateView):
    template_name = "configuracion/create-user.html"
    form_class = CrearUsuario
    success_message = 'Usuario Creado.'
    success_url = reverse_lazy('crear-usuario')

    def form_valid(self, form):
        response = super().form_valid(form)
        user_pk = form.instance.pk
        user = User.objects.get(pk=user_pk)
        perfil = Perfil(
            rol_usuario= form.cleaned_data['rol_usuario'],
            usuario= user
        )
        perfil.save()
        return response
    
class UsuarioLista(ProyectoMixin, ListView):
    model = User
    template_name = 'configuracion/list-user.html'
    context_object_name = 'usuarios'

class UsuarioEdit(ProyectoMixin, UpdateView):
    model = User
    template_name = 'configuracion/edit-user.html'
    success_url = reverse_lazy('listar-usuarios')
    form_class = EditUsuario

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            user_pk = form.instance.pk
            user = User.objects.get(pk=user_pk)
            perfil = Perfil.objects.get(usuario=user)
            perfil.rol_usuario = form.cleaned_data['rol_usuario']
            perfil.save()
        except Perfil.DoesNotExist:
            pass
        return response

class UsuarioDelete(ProyectoMixin, DeleteView):
    model = User
    template_name = 'configuracion/delete-user.html'
    success_url = reverse_lazy('listar-usuarios')
    context_object_name = 'usuario'
    
    def post(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return self.success_url
    