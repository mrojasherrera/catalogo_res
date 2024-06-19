from django.contrib import admin
from .models import Resoluciones, ResolucionRelacion

# Register your models here.

# definir que se muestra en el admin
class ResolucionesAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha", "sumario", "origen", "texto_de_resolucion")

admin.site.register(Resoluciones)
admin.site.register(ResolucionRelacion)