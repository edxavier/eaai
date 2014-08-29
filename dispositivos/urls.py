from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',    
	#url(r'api-auth/'), include('rest_framework.urls',namespace='rest_framework')),
    #CATEGORIA
    url(r'^listar$', login_required(listarDispositivos.as_view()), name='list_dispositivos'),
    url(r'^([-\w]+)/$', login_required(detallesDispositivos.as_view()), name='detalle_dispositivo'),
   #url(r'^sistemas/', ListarCategoria.as_view(), name='list_categoria'),
    # url(r'^eaai/', include('eaai.foo.urls')),

)
