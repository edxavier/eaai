# Create your views here.
from .models import *
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.template.loader import get_template
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

class listarDispositivos(TemplateView):
	def get(self, request): 
		page_title = 'Dispositivos'
		page_sub_title= 'Lista de Dispositivos' 
		devices= Dispositivo.objects.filter(activo=True).order_by('nombre',)
		return render_to_response('dispositivos/listDispositivos.html', locals(),context_instance=RequestContext(request))

class detallesDispositivos(TemplateView):
	def get(self, request,dis_pk): 
		page_title = 'Dispositivos'
		page_sub_title= 'Detalles de Dispositivo' 
		device =get_object_or_404(Dispositivo, pk=dis_pk,activo=True,)
		components =Componente_hardware.objects.filter(activo=True,dispositivo__pk=device.pk).order_by('creado',)
		return render_to_response('dispositivos/detalle.html', locals(),context_instance=RequestContext(request))

