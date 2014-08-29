# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from django.template.context import RequestContext
from django.template.loader import get_template
from django.core.urlresolvers import reverse_lazy
from .models import *


class ListarCategorias(ListView):
	page_title = 'Sistemas'
	page_sub_title= 'Lista de Categorias' 
	template_name= 'sistemas/categoria/listCategoria.html'
	queryset= Categoria.objects.all().order_by('name', 'created_at')
	context_object_name= 'categorias'

class ListarSistemas(TemplateView):
	def get(self, request): 
		page_title = 'Sistemas'
		page_sub_title= 'Lista de Sistemas' 
		#categorias= Categoria.objects.all().order_by('name', 'created_at')
		sistemas= Sistema.objects.all().order_by('name', 'created_at')
		return render_to_response('sistemas/sistema/listSistema.html', locals(),context_instance=RequestContext(request))

class FiltrarSistemas_X_Categoria(TemplateView):
	def get(self, request,idcategoria): 
		print "filtr Sis"
		page_title = 'Sistemas'
		page_sub_title= 'Sistemas por categoria' 
		#categorias= Categoria.objects.all().order_by('name', 'created_at')
		cat= get_object_or_404(Categoria, pk=idcategoria)
		sistemas= Sistema.objects.filter(category=cat)
		return render_to_response('sistemas/sistema/listSistema.html', locals(),context_instance=RequestContext(request))

class DetalleSistema(TemplateView):
	def get(self, request,idSistema): 
		page_title = 'Sistemas'
		page_sub_title= 'Detalles' 
		#Categoria.objects.all().order_by('name', 'created_at')
		sistema= get_object_or_404(Sistema, pk=idSistema)
		detalle=True
		return render_to_response('sistemas/sistema/listSistema.html', locals(),context_instance=RequestContext(request))
