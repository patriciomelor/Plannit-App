from django.urls import path, include
from . import views

urlpatterns = [
    #URL DE USUARIOS
    path('listado-user/', views.UsuarioLista.as_view(), name='listar-usuarios'),
    path('invitation-user/', views.InvitationView.as_view(), name='invitar-usuarios'),
    path('nuevo-user/', views.UsuarioView.as_view(), name='crear-usuario'),
    path('editar-user/<pk>/', views.UsuarioEdit.as_view(), name='editar-usuario'),
    path('eliminar-user/<pk>/', views.UsuarioDelete.as_view(), name='eliminar-usuario'),
    path('detalle-user/<pk>/', views.UsuarioDetail.as_view(), name ='detalle-usuario'),
    #URL DE PROYECTOS
    path('proyecto-detalle/<pk>/', views.ProyectoDetail.as_view(), name='detalle-proyecto'),
    path('proyecto-editar/<pk>/', views.ProyectoEdit.as_view(), name='editar-proyecto'),
    path('proyecto-lista', views.ProyectoList.as_view(), name='lista-proyecto'),
    path('proyecto-delete/<pk>/', views.ProyectoDelete.as_view(), name='delete-proyecto'),
    path('proyecto-create/', views.ProyectoCreate.as_view(), name='crear-proyecto'),
    path('proyecto-add-user/', views.UsuarioAdd.as_view(), name='add-user-proyecto'),
    path('proyecto-remove-user/', views.UsuarioRemove.as_view(), name='remove-user-proyecto'),
    #URL DE CONFIG
    path('restricciones/', views.RestriccionesView.as_view() , name='restriccion'),
    path('restricciones-edit/<pk>/', views.RestriccionesEdit.as_view() , name='restriccion-edit'),
    path('restricciones-delete/<pk>/', views.RestriccionesDelete.as_view() , name='restriccion-delete'),
    path('no-cumplimiento/', views.NoCumplimientoView.as_view() , name='no-cumplimiento'),
    path('no-cumplimiento-edit/<pk>/', views.NoCumplimientoEdit.as_view() , name='no-cumplimiento-edit'),
    path('no-cumplimiento-delete/<pk>/', views.NoCumplimientoDelete.as_view() , name='no-cumplimiento-delete'),
    path('umbrales/', views.UmbralIndexList.as_view(), name='list-umbrales'),
    path('edit-umbrales/<pk>/', views.UmbralesEdit.as_view(), name='edit-umbrales'),
]


