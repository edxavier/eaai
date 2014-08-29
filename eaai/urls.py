from django.conf.urls import patterns, include, url
from eaai import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from bitacora.views import CategoryViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categorias', CategoryViewSet)
router.register(r'usuarios', UserViewSet)
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', home.as_view(), name='home'),
    #url(r'^', 'django.contrib.auth.views.login', {'template_name':'index.html'},name='login'),
   # url(r'^logout/', 'django.contrib.auth.views.logout', name='logout'),
    # url(r'^eaai/', include('eaai.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'api/', include(router.urls)),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    	{ 'document_root' : settings.MEDIA_ROOT  }),

    url(r'^bitacora/', include('bitacora.urls')),
    url(r'^sistemas/', include('sistemas.urls')),
    url(r'^dispositivos/', include('dispositivos.urls')),
    url(r'^', include('usuario.urls')),
    url(r'^select2/', include('django_select2.urls')),

)
