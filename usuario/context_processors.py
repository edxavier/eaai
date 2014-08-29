from sistemas.models import Categoria
from django.contrib.auth.models import User
from eaai import settings
from django.shortcuts import render_to_response,get_object_or_404

def eaai(request):
	"""try:
		perfil =get_object_or_404(Perfil, usuario=request.user)
	except Exception, e:
		perfil=None"""

	return {
	    'categorias': Categoria.objects.filter(is_active=True).order_by('name', 'created_at'),
	    'usuarios': User.objects.filter(is_active=True).order_by('-perfil__fecha_nacimiento','username',),
	    #'perfil': perfil,
	    'site_name': settings.SITE_NAME,
	    'meta_keywords': settings.META_KEYWORDS,
	    'meta_description': settings.META_DESCRIPTION,
	    'page_title' :'Inicio',
		'page_sub_title':'Pagina de Inicio',
	    'request': request
    }
	 