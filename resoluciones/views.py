# views.py
from django.shortcuts import get_object_or_404, render
from .models import Resoluciones, ResolucionRelacion
from .forms import ResolucionesFilterForm

def resoluciones_list(request):
    form = ResolucionesFilterForm(request.GET or None)
    resoluciones = Resoluciones.objects.all()
    # 
    # if form.is_valid():
    #     if form.cleaned_data['numero']:
    #         resoluciones = resoluciones.filter(numero=form.cleaned_data['numero'])
    #     if form.cleaned_data['sumario']:
    #         resoluciones = resoluciones.filter(sumario__icontains=form.cleaned_data['sumario'])
    #     if form.cleaned_data['fecha_publicacion']:
    #         resoluciones = resoluciones.filter(fecha_publicacion=form.cleaned_data['fecha_publicacion'])
    #     if form.cleaned_data['origen']:
    #         resoluciones = resoluciones.filter(origen=form.cleaned_data['origen'])
    #     if form.cleaned_data['texto_de_resolucion']:
    #         resoluciones = resoluciones.filter(origen=form.cleaned_data['texto_de_resolucion'])
    #     if form.cleaned_data['observaciones']:
    #         observaciones = resoluciones.filter(observaciones__icontains=form.cleaned_data['observaciones'])
    # 
    
    if form.is_valid():
        numero = form.cleaned_data.get('numero')
        sumario = form.cleaned_data.get('sumario')
        fecha_publicacion = form.cleaned_data.get('feha_publicacion')
        observaciones = form.cleaned_data.get('observaciones')
        origen = form.cleaned_data.get('origen')

        if numero:
            resoluciones = resoluciones.filter(numero=numero)
        if sumario:
            resoluciones = resoluciones.filter(sumario__icontains=sumario)
        if fecha_publicacion: 
            resoluciones = resoluciones.filter(fecha_publicacion=fecha_publicacion)
        if observaciones:
            resoluciones = resoluciones.filter(observaciones__icontains=observaciones)
        if origen:
            resoluciones = resoluciones.filter(origen__in=origen)



    return render(request, 'resoluciones/resoluciones_list.html', {'resoluciones': resoluciones, 'form': form})
# 
# 
def resolucion_detalle(request, resolucion_id):
    resolucion = get_object_or_404(Resoluciones, id=resolucion_id)
    relacionadas = ResolucionRelacion.objects.filter(res_orig=resolucion)
    return render(request, 'resolucion_detalle.html', {'resolucion': resolucion, 'relacionadas': relacionadas})