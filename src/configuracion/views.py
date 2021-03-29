from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import FormView, CreateView, DeleteView, UpdateView, ListView, DetailView, FormView
from panel_carga.views import ProyectoMixin
from django.contrib.auth.models import User, Group, Permission, PermissionsMixin
from .roles import ROLES
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.conf import settings 
from django.template.loader import render_to_string
from django.core.mail import send_mail 
from panel_carga.models import *
from panel_carga.forms import ProyectoForm
from bandeja_es.models import *


from .models import Perfil
from .forms import CrearUsuario, EditUsuario, InvitationForm
from invitations.utils import get_invitation_model
from tools.objects import StaffViewMixin, SuperUserViewMixin, is_staff_check, is_superuser_check

class UsuarioView(ProyectoMixin, CreateView):
    template_name = "configuracion/create-user.html"
    form_class = CrearUsuario
    success_message = 'Usuario Creado.'
    success_url = reverse_lazy('crear-usuario')
    
    def form_valid(self, form):
        context = {}
        response = super().form_valid(form)
        user_pk = form.instance.pk
        user = User.objects.get(pk=user_pk)
        rol = form.cleaned_data['rol_usuario']
        company = form.cleaned_data['empresa']
        perfil = Perfil(
            usuario=form.instance,
            rol_usuario=rol,
            empresa=company,
            client=True
        )
        perfil.save()
        return response

class UsuarioEdit(ProyectoMixin, UpdateView):
    model = User
    template_name = 'configuracion/edit-user.html'
    success_url = reverse_lazy('listar-usuarios')
    form_class = EditUsuario

    def form_valid(self, form):
        response = super().form_valid(form)
        rol = form.cleaned_data['rol_usuario']
        print(rol)
        company = form.cleaned_data['empresa']
        perfil = Perfil.objects.get(usuario=form.instance)
        perfil.rol_usuario = rol
        perfil.empresa = company
        perfil.save()
        return response
    
class UsuarioLista(ProyectoMixin, ListView):
    model = User
    template_name = 'configuracion/list-user.html'
    context_object_name = 'usuarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["codigo_proyecto"] = self.proyecto.codigo
        return context

class UsuarioDelete(ProyectoMixin, DeleteView):
    model = User
    template_name = 'configuracion/delete-user.html'
    success_url = reverse_lazy('listar-usuarios')
    context_object_name = 'usuario'
    
class UsuarioDetail(ProyectoMixin, DetailView):
    model = User
    template_name = 'configuracion/detail-user.html'
    context_object_name = "usuario"

    def get_context_data(self, **kwargs):
        user = self.get_object()
        grupos = user.groups.all()
        print(grupos)
        context["grupos"] = grupos
        return context

# Añade usuarios al proyecto actual seleccionado
class UsuarioAdd(ProyectoMixin, ListView):
    model = User
    template_name = 'configuracion/add-lista_usuario.html'
    success_message = 'Usuarios añadidos correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_list = []
        all_users = User.objects.all()
        current_users = self.proyecto.participantes.all()
        for user in all_users:
            if not user in current_users:
                user_list.append(user)

        context['users'] = user_list
        return context
    
    def post(self, request, *args, **kwargs):
        usuario_ids = self.request.POST.getlist('id[]')
        for usuario in usuario_ids:
            user = User.objects.get(pk=usuario)
            proyecto_add = self.proyecto
            proyecto_add.participantes.add(user)
        return redirect('listar-usuarios')

class ProyectoList(ProyectoMixin, ListView):
    context_object_name = 'proyectos'
    template_name = 'configuracion/list-proyecto.html'
    queryset = Proyecto.objects.all().order_by('-fecha_inicio')

class ProyectoDetail(ProyectoMixin, DetailView):
    template_name='configuracion/detail-proyecto.html'       
    context_object_name = 'proyecto'

class ProyectoEdit(ProyectoMixin, UpdateView):
    template_name = 'configuracion/edit-proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('lista-proyecto')
    success_message = 'Información del Proyecto Actualizada'

class ProyectoDelete(ProyectoMixin, DeleteView):
    template_name = 'configuracion/delete-proyecto.html'
    success_message = 'Proyecto Eliminado'
    success_url = reverse_lazy('lista-proyecto')

    def delete(self, request, *args, **kwargs):
        objeto = self.get_object()
        if objeto == proyecto:
            messages.add_message(request, messages.ERROR, 'No se puede eliminar el proyecto seleccionado.')
            return redirect('lista-proyecto')
        else:  
            return super(ProyectoDelete, self).delete(request, *args, **kwargs)

class ProyectoCreate(ProyectoMixin, CreateView):
    template_name = 'configuracion/create-proyecto.html'
    success_message = 'Proyecto Creado correctamente'
    success_url = reverse_lazy('lista-proyecto')
    form_class = ProyectoForm

class InvitationView(ProyectoMixin, FormView):
    template_name = 'configuracion/invitation_form.html'
    success_message = 'Invitación enviada correctamente'
    success_url = reverse_lazy('listar-usuarios')
    form_class = InvitationForm

    def form_valid(self, form):
        invitation = get_invitation_model()
        response = super().form_valid(form)
        nombre = form.cleaned_data['nombres']
        correo = form.cleaned_data['correo']
        invite = invitation.create(correo, inviter=self.request.user)
        invite.send_invitation(self.request)
        return response 