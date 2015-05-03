from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',    
	#url(r'api-auth/'), include('rest_framework.urls',namespace='rest_framework')),
    #CATEGORIA
    url(r'^listar$', login_required(listarDispositivos.as_view()), name='list_dispositivos'),
    url(r'^listar/componentes$', login_required(listarComponentesHW.as_view()), name='list_componentes'),
    url(r'^(\d+)/historial/nuevo/$', login_required(NuevoHistorialDispositivo.as_view()), name='nuevo_historial'),
    #url(r'^([-\w]+)/$', login_required(detallesDispositivos.as_view()), name='detalle_dispositivo'),
    url(r'^(?P<dis_pk>[-\w]+)/$', login_required(detallesDispositivos.as_view()), name='detalle_dispositivo'),
    #la url de arriva significa qye se recibe el parametro dis_pk que sea  1 o mas digitos (d para enteros y w para cualquier alfanumeroco)
   #url(r'^sistemas/', ListarCategoria.as_view(), name='list_categoria'),
    # url(r'^eaai/', include('eaai.foo.urls')),

)
