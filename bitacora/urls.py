from django.conf.urls import patterns, include, url
from bitacora.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    #url(r'^notas/', 'bitacora.views.home', name='home'),
   # url(r'^notas/', index.as_view(), name='home'),
    
	#url(r'api-auth/'), include('rest_framework.urls',namespace='rest_framework')),
    #CATEGORIA
    url(r'^notas/$', login_required(ListarNotas.as_view()), name='list_notas'),
    url(r'^notas/por-categoria/(\d+)/$',  login_required(FiltrarNotas_x_Categoria.as_view()), name='filter_notas'),
    url(r'^notas/(\d+)/$',  login_required(DetalleNota.as_view()), name='detail_nota'),
    url(r'^notas/nueva/$',  login_required(NuevaNota.as_view()), name='new_nota'),
    url(r'^notas/busqueda/$',  login_required(BusquedaAvanzada.as_view()), name='search_notas'),
    url(r'^estadisticas/$', Estadistica_Notas.as_view()),
    url(r'^estadisticas/usuario$', Estadistica_NotasXUsuario.as_view()),
    url(r'^estadisticas/sistemas$', Estadistica_Sistemas.as_view()),
    url(r'^([-\w]+)/$',  login_required(GetTemplate.as_view()), name='template'),
    # url(r'^eaai/', include('eaai.foo.urls')),

)
