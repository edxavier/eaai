import os
import StringIO
from unipath import Path
from xhtml2pdf import pisa   
from django.conf import settings
from django.template import Context
from .models import *
from mongoengine import *
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import get_template
from django.core.urlresolvers import reverse_lazy
from initData import autoCreateEmp_Horario, getRolIndex
from dateutil import parser
import datetime
from datetime import date, timedelta
from django.views.decorators.csrf import csrf_exempt




class VerMatriz(TemplateView):
    def get(self, request): 
        matriz= MatrizHorario.objects
        return render_to_response('horario/matriz.html', locals(),context_instance=RequestContext(request))


class VerHorario(TemplateView):
    def get(self, request): 
        horarios= Horario.objects
        valides= Horario.objects.first()
        semanas=[]
        horario_semana=[]
        for s in range(0,13):
            ini=s*7
            fin=ini+7
            horario_semana=[]
            for h in horarios:
                #print "Inicio "+ini.__str__()+" Fin "+ fin.__str__()
                turno=Turnos()
                te=h.empleado.horario_emp[ini:fin]
                horario_semana.append({"horario":te,"nombre":h.empleado.nombre,"tareas":h.empleado.tareas})
            semanas.append({"semanaH":horario_semana})
        return render_to_response('horario/horario.html', locals(),context_instance=RequestContext(request))


class VerGenerador(TemplateView):
    def get(self, request): 
        emps= Horario.objects.first()
        hoy= datetime.datetime.now()
        fechaDisp= (emps.fecha_final - timedelta(days=10))
        daysDiff = fechaDisp - hoy

        return render_to_response('horario/generarHorario.html', locals(),context_instance=RequestContext(request))

    def post(self,request,*args,**kwargs):
        semanas=int(request.POST['quantity'])
        autoCreateEmp_Horario(semanas)
        return  HttpResponseRedirect(reverse_lazy('ver_horario'))



# Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
def link_callback(uri, rel):
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.RUTA_STATIC   # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
       # path = os.path.join(mRoot, uri.replace(mUrl, ""))
        path=sRoot
       # print "######################funciooooooooooooooooooooonaaaa es algo del mierda packete MEDIA"
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
        #print "######################funciooooooooooooooooooooonaaaa es algo del mierda packete STATIC :"+path

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % \
                    (sUrl, mUrl))
    return path

class HorarioPDF(TemplateView):
    def get(self, request):
        horarios= Horario.objects
        valides= Horario.objects.first()
        mesHorario=valides.fecha_final - timedelta(days=10)
        semanas=[]
        horario_semana=[]
        data={}
        for s in range(0,valides.semanas):
            ini=s*7
            fin=ini+7
            horario_semana=[]
            for h in horarios:
                #print "Inicio "+ini.__str__()+" Fin "+ fin.__str__()
                turno=Turnos()
                te=h.empleado.horario_emp[ini:fin]
                horario_semana.append({"horario":te,"nombre":h.empleado.nombre})
            semanas.append({"semanaH":horario_semana})

        data['horario']=semanas
        data['valides']=mesHorario
        template = get_template('horario/horarioPDF.html')

        html  = template.render(Context(data))

        # Write PDF to file
        file = open(os.path.join(settings.MEDIA_ROOT, 'horario.pdf'), "w+b")
        pisaStatus = pisa.CreatePDF(html, dest=file,
                link_callback = link_callback)

        # Return PDF document through a Django HTTP response
        file.seek(0)
        pdf = file.read()
        file.close()            # Don't forget to close the file handle
        return HttpResponse(pdf, mimetype='application/pdf')

class MatrizPDF(TemplateView):
    def get(self, request):
        # Prepare context
        matriz= MatrizHorario.objects
        data = {}
        data['matriz'] =matriz
       
        # Render html content through html template with context
       
        template = get_template('horario/matrizPDF.html')

        html  = template.render(Context(data))

        # Write PDF to file
        file = open(os.path.join(settings.MEDIA_ROOT, 'matriz.pdf'), "w+b")
        pisaStatus = pisa.CreatePDF(html, dest=file,
                link_callback = link_callback)

        # Return PDF document through a Django HTTP response
        file.seek(0)
        pdf = file.read()
        file.close()            # Don't forget to close the file handle
        return HttpResponse(pdf, mimetype='application/pdf')

class saveMachinereboots(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(saveMachinereboots, self).dispatch(*args, **kwargs)
            
    def post(self,request,*args,**kwargs):
        semanas=request.POST['event']
        print semanas
        return  HttpResponse("Ok")