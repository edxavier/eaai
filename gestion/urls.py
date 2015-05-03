from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
	
    url(r'^boot_event/', Nodes_boots.as_view(),name='boot_hist'), 
    url(r'^hosts/', Host_list.as_view(),name='hosts_list'), 
    url(r'^hosts_large/', Host_cuadricula.as_view(),name='hosts_cuadricula'), 
    url(r'^(?P<host_ip>[a-zA-Z0-9_.-]+)/$', Host_details.as_view(),name='hosts_detail'), 
    url(r'^json/(?P<option>[a-z]+)/(?P<ip>[a-zA-Z0-9_.-]+)/$', Json_data.as_view(),name=''), 

)
