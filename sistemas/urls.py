from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    #url(r'^notas/', 'bitacora.views.home', name='home'),
   # url(r'^notas/', index.as_view(), name='home'),
    
	#url(r'api-auth/'), include('rest_framework.urls',namespace='rest_framework')),
    #CATEGORIA
    url(r'^$', login_required(ListarSistemas.as_view()), name='list_sistemas'),
    url(r'^por-categoria/(\d+)/', login_required(FiltrarSistemas_X_Categoria.as_view()), name='filter_sistemas'),
    url(r'^(\d+)/', login_required(DetalleSistema.as_view()), name='detail_sistema'),
    url(r'^categorias/', login_required(ListarCategorias.as_view()), name='list_categorias'),
   #url(r'^sistemas/', ListarCategoria.as_view(), name='list_categoria'),
    # url(r'^eaai/', include('eaai.foo.urls')),

)
