from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prueba

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/bienvenida.html'

class PruebaListView(ListView):
    template_name = 'home/listado.html'
    queryset = ['A', 'B', 'C', 'D']
    context_object_name = 'listado'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = 'home/pruebas.html'
    context_object_name = 'lista_prueba'