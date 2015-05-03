# Create your views here.
from .models import *
from .forms import *
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.template.loader import get_template
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

class listarDispositivos(TemplateView):
	def get(self, request): 
		page_title = 'Dispositivos'
		page_sub_title= 'Lista de Dispositivos' 
		devices= Dispositivo.objects.filter(activo=True).order_by('nombre',)
		return render_to_response('dispositivos/listDispositivos.html', locals(),context_instance=RequestContext(request))

class listarComponentesHW(TemplateView):
	def get(self, request): 
		page_title = 'Componentes'
		page_sub_title= 'Lista de Componentes' 
		componentes= Componente_hardware.objects.filter(activo=True).order_by('creado',)
		return render_to_response('dispositivos/componentes.html', locals(),context_instance=RequestContext(request))

class detallesDispositivos(TemplateView):
	def get(self, request,dis_pk): 
		page_title = 'Dispositivos'
		page_sub_title= 'Detalles de Dispositivo' 
		device =get_object_or_404(Dispositivo, serie=dis_pk,activo=True,)
		components =Componente_hardware.objects.filter(activo=True,dispositivo__pk=device.pk).order_by('creado',)
		return render_to_response('dispositivos/detalle.html', locals(),context_instance=RequestContext(request))

class NuevoHistorialDispositivo(TemplateView):
	def get(self, request,id_dev): 
		page_title = 'Dispositivos'
		page_sub_title= 'Historial de Dispositivo'
		device =get_object_or_404(Dispositivo, pk=id_dev,activo=True,)
		historia=Historial_equipo()
		historia.dispositivo=device
		historia.estado_antes=device.estado
		historia.ubicacion_antes=device.ubicacion
		form = Historial_Form(instance=historia)
		return render_to_response('dispositivos/nuevoHistorial.html', locals(),context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		form= Historial_Form(request.POST)
		if form.is_valid():
			hist=form.save(commit=False)
			hist.usuario=request.user
			device =get_object_or_404(Dispositivo, pk=hist.dispositivo.pk,activo=True,)
			device.estado=hist.estado_despues
			device.ubicacion=hist.ubicacion_despues
			device.save()
			hist.save()
			return  HttpResponseRedirect("/dispositivos/"+str(hist.dispositivo.pk))
		else:
			return render_to_response('dispositivos/nuevoHistorial.html', locals(),context_instance=RequestContext(request))			