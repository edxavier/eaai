# Create your views here.
# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template.context import RequestContext
from django.template.loader import get_template
from django.core.urlresolvers import reverse_lazy
from usuario.models import Perfil
from usuario.forms import *
from django.contrib.auth.forms import PasswordChangeForm

#def home(request):
    #return HttpResponse("<h2>HOME</h2>")
#   return render_to_response('index.html', context_instance=RequestContext(request))



class perfil(TemplateView):
    @method_decorator(login_required)
    def get(self, request):     
        page_title = 'Perfil'
        page_sub_title= 'Perfil de Usuario'
        return render_to_response('usuario/perfil.html', locals(),context_instance=RequestContext(request))


class ActualizarPerfil(FormView):
    #esto hace que cuendo se acceda a la clase se requiera de un login, de lo contrario habria que ponerlo en cada metodo
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ActualizarPerfil, self).dispatch(*args, **kwargs)

    
    def get(self, request): 
        page_title = 'Perfil'
        page_sub_title= 'Actualizar Perfil'        
        form = PerfilForm(instance=request.user.perfil)
        return render_to_response('usuario/actualizarPerfil.html', locals(),context_instance=RequestContext(request))
    
    
    def post(self,request, *args,**kwargs):
        page_title = 'Perfil'
        page_sub_title= 'Actualizar Perfil'
        #obtener nombres, appellidos y Email ya q no son parte del modelo pero vienen en el post
        nombres= request.POST['nombres']
        apellidos= request.POST['apellidos']
        email= request.POST['email']
        #inicializar el dormulario con con el perfil del usuario y asignar los datos del post
        form = PerfilForm(request.POST,request.FILES,instance=Perfil.objects.get(usuario=request.user))
        if form.is_valid():
            form.save()
            usuario=request.user
            usuario.first_name=nombres
            usuario.last_name=apellidos
            usuario.email=email
            usuario.save()
            return  HttpResponseRedirect(reverse_lazy('perfil'))
        else:
            #perfil = get_object_or_404(Perfil, usuario=request.user)
            return render_to_response('usuario/actualizarPerfil.html', locals(),context_instance=RequestContext(request))


class Changepassword (FormView):
    @method_decorator(login_required)
    def get(self, request): 
        page_title = 'Perfil'
        page_sub_title= 'Cambio de clave'
       # perfil = get_object_or_404(Perfil, usuario=request.user)
        form = PasswordChangeForm(user=request.user)
        return render_to_response('usuario/CambiarClave.html', locals(),context_instance=RequestContext(request))   
    
    @method_decorator(login_required)
    def post(self, request):    
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse_lazy('perfil'))
        else:
            page_title = 'Perfil'
            page_sub_title= 'Cambio de <clave></clave>'
           # perfil = get_object_or_404(Perfil, usuario=request.user)
            return render_to_response('usuario/CambiarClave.html', locals(),context_instance=RequestContext(request))   

