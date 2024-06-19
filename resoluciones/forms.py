# forms.py
from django import forms
from .models import Resoluciones

class ResolucionesFilterForm(forms.Form):
    numero = forms.CharField(
        required=False, 
        label='Número',
        widge=forms.TextInput(attrs={'autocomplete': 'off'}))
    sumario = forms.CharField(
        max_length=500, 
        required=False, 
        label='Sumario',
        widget=forms.TextInput(attrs={'autocomplete':'off', 'size':'40'})
        )
    fecha_publicacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de Publicación')
    # origen = forms.CharField(max_length=4, required=False, label='Origen')
    origen = forms.MultipleChoiceField(
        choices=Resoluciones.Origen.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False, 
        label='Origen'
    )
    texto_de_resolucion = forms.CharField(max_length=100, required=False, label='Texto de Resolución')
    observaciones = forms.CharField(
        max_length=500, 
        required=False, 
        label='Observaciones',
        widget=forms.TextInput(attrs={'size': '70'})
        )