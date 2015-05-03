from django.contrib import admin
from .models import *
from .forms import *


class HistorialAdmin (admin.ModelAdmin):
    list_display=('id','tipo_entrada','usuario','creado',)
    list_filter=('usuario__username','dispositivo')
    search_fields=('usuario__username','descripcion','dispositivo__nombre')

    list_per_page = 10
    ordering = ['-creado']
    date_hierarchy = 'creado'
    form = Historial_equipo_AdminFRM
    #raw_id_fields=('systems',)
    #sobreescribir la funcion del formAdmin para indicar el usuario que esta haciendo la operaciony no que lo haga el mismo
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        try:
            #instentar salvar si ya es una actualizacion de lo contrario se dispara una exeption
            if  instance.usuario:
                instance.save()
        except Exception, e:
            instance.usuario=request.user
            instance.save()
        
        return instance

class DispositivoAdmin (admin.ModelAdmin):
    list_display=('id','serie','nombre','usuario','creado',)
    list_filter=('usuario__username','creado','ubicacion')
    search_fields=('usuario__username','descripcion','serie','nombre')
    list_display_links = ('serie',)
    list_per_page = 10
    ordering = ['-creado']
    date_hierarchy = 'creado'
    form = DispositivoAdminFRM
    #raw_id_fields=('systems',)
    #sobreescribir la funcion del formAdmin para indicar el usuario que esta haciendo la operaciony no que lo haga el mismo
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        try:
            #instentar salvar si ya es una actualizacion de lo contrario se dispara una exeption
            if  instance.usuario:
                instance.save()
        except Exception, e:
            instance.usuario=request.user
            instance.save()
        
        return instance

admin.site.register(Tipo_Dispositivo)
admin.site.register(Historial_equipo,HistorialAdmin)
admin.site.register(Tipo_Componente)
admin.site.register(Dispositivo,DispositivoAdmin)
admin.site.register(Componente_hardware)
