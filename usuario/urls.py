from django.conf.urls import patterns, include, url
from usuario.views import *
from django.contrib.auth.forms import AdminPasswordChangeForm

urlpatterns = patterns('',
    

    # Examples:
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'index.html'},name='login'),
    
    url(r'^salir/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^perfil/$', perfil.as_view(), name='perfil'),
    url(r'^perfil/actualizar$', ActualizarPerfil.as_view(), name='actualizar_perfil'),
    url(r'^perfil/cambio-de-clave$', Changepassword.as_view(), name='actualizar_clave'),

   # url(r'^notas/', index.as_view(), name='home'),

 

)
