# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView,FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template.context import RequestContext
from django.template.loader import get_template
from django.core.urlresolvers import reverse_lazy
from bitacora.forms import *
from bitacora.models import *
from sistemas.models import *
from django.contrib.auth.models import User
from .serializers import CategorySerializer, UserSerializer
from rest_framework import viewsets
from django.db.models import Q
import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


#def home(request):
	#return HttpResponse("<h2>HOME</h2>")
#	return render_to_response('index.html', context_instance=RequestContext(request))
class UserViewSet(viewsets.ModelViewSet):
	queryset= User.objects.all()
	serializer_class= UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset= Categoria.objects.all()
	serializer_class= CategorySerializer

class GetTemplate(TemplateView):
	def get(self, request,Thetemplate): 
		Thetemplate+=".html"
		return render_to_response('bitacora/'+Thetemplate, locals(),context_instance=RequestContext(request))

class ListarNotas(ListView):
	def get(self, request):
		page_title = 'Bitacora'
		page_sub_title= 'Ultimas 100 notas' 
		template= 'bitacora/notas.html'
		notas= Nota.objects.all()[:100]
		return render_to_response(template, locals(),context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		page_title = 'Bitacora'
		termino=request.POST['search_text']
		page_sub_title= 'Resultados para:  %s' %(termino)
		notas= Nota.objects.filter(Q(keywords__contains=termino) | Q(description__contains=termino)).distinct()[:100] #
		return render_to_response('bitacora/notas.html', locals(),context_instance=RequestContext(request))


class NuevaNota(FormView):
	def get(self, request): 
		page_title = 'Bitacora'
		page_sub_title= 'Agregar nueva anotacion'
		sistemas= Sistema.objects.filter(is_active=True)
		#estados = Severidad_nota.objects.filter(is_active=True)
		form= NotaForm2()
		#notas= Nota.objects.filter(systems_category_name=cat.name)
		return render_to_response('bitacora/nueva.html', locals(),context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		form= NotaForm2(request.POST,request.FILES)
		if form.is_valid():
			nota=form.save(commit=False)
			nota.user=request.user
			nota.save()
			form.save_m2m()
			#subject, from_email, to = 'Bitacora Electronica', 'from@example.com', 'edxrojas@yahoo.es'
			#text_content = 'This is an important message.'
			#html_content = nota.description
			#msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			#msg.attach_alternative(html_content, "text/html")
			#msg.send()
			return  HttpResponseRedirect(reverse_lazy('list_notas'))
		else:
			return render_to_response('bitacora/nueva.html', locals(),context_instance=RequestContext(request))


class FiltrarNotas_x_Categoria(TemplateView):
	def get(self, request,idcategoria): 
		page_title = 'Bitacora'
		cat= get_object_or_404(Categoria, pk=idcategoria)
		page_sub_title= 'Notas por categoria:  %s' %(cat.name)
		sistemas= Sistema.objects.filter(category=cat)
		notas= Nota.objects.filter(systems__in=sistemas).distinct()[:100] #
		#notas= Nota.objects.filter(systems_category_name=cat.name)
		return render_to_response('bitacora/notas.html', locals(),context_instance=RequestContext(request))

class DetalleNota(TemplateView):
	def get(self, request,idNota): 
		page_title = 'Bitacora'
		nota= get_object_or_404(Nota, pk=idNota)
		page_sub_title= 'Detalles de nota  %d' %(nota.pk)
		#obtener todos los sistemas que estan en la nota
		sistemas = Sistema.objects.filter(nota__pk=nota.pk)
		return render_to_response('bitacora/detalleNota.html', locals(),context_instance=RequestContext(request))

class BusquedaAvanzada(TemplateView):
	def get(self, request): 
		page_title = 'Bitacora'
		page_sub_title= 'Busqueda especificas'
		return render_to_response('bitacora/busqueda.html', locals(),context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		page_title = 'Bitacora'
		inicio=request.POST['fecha_inicial']
		fin=request.POST['fecha_final']
		termino=request.POST['search_text'].strip()
		page_sub_title= 'Resultados para el rango '+inicio+' - '+ fin
		inicio= inicio+':00-0600'		
		fin= fin+':00-0600'
		if termino and not termino.isspace():
			notas= Nota.objects.filter(created_at__range=[inicio,fin]).filter(Q(keywords__contains=termino) | Q(description__contains=termino)).distinct()[:100]
		else:
			notas= Nota.objects.filter(created_at__range=[inicio,fin]).distinct()[:100]
		
		return render_to_response('bitacora/busqueda.html', locals(),context_instance=RequestContext(request))