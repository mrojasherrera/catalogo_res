# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('resoluciones/', views.resoluciones_list, name='resoluciones_list'),
    path('resoluciones/<int:resolucion_id>', views.resolucion_detalle, name='resolucion_detalle'),
]
