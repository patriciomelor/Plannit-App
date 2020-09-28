from django import forms
from .models import Proyecto, Documento

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'