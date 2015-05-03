from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	
    url(r'^matriz/', login_required(VerMatriz.as_view()), name='ver_matriz'),
    url(r'^pdf/matriz', login_required(MatrizPDF.as_view()), name=''),
    url(r'^pdf/horario', login_required(HorarioPDF.as_view()), name='ver_horarioPDF'),
    url(r'^horario/', login_required(VerHorario.as_view()), name='ver_horario'),
    url(r'^generar/', login_required(VerGenerador.as_view()), name='ver_generador'),

)
