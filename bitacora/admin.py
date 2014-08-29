from django.contrib import admin
from bitacora.models import *
from bitacora.forms import NotaForm,EstadoForm


class SeverityAdmin (admin.ModelAdmin):
    list_display=('name','description','creado_por','created_at', 'updated_at',)
    #list_filter=('user__username',)
    search_fields=('user__username',)
    list_display_links = ('name',)
    list_per_page = 10
    ordering = ['name']
   # prepopulated_fields = {'slug' : ('name',)}
    date_hierarchy = 'created_at'
    form=EstadoForm
    
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        try:
            #instentar salvar si ya es una actualizacion de lo contrario se dispara una exeption
            if  instance.pk:
                instance.save()
            else:
                instance.user=request.user
                instance.save()
        except Exception, e:
            return
        
        return instance


class NotaAdmin (admin.ModelAdmin):
    list_display=('id','creado_por','created_at', 'updated_at','sistemas_involucrados',)
    #list_filter=('user__username',)
    search_fields=('user__username','keywords')
    list_per_page = 10
    filter_horizontal= ('systems',)
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    form = NotaForm
    #raw_id_fields=('systems',)
    #sobreescribir la funcion del formAdmin para indicar el usuario que esta haciendo la operaciony no que lo haga el mismo
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        try:
            #instentar salvar si ya es una actualizacion de lo contrario se dispara una exeption
            if  instance.user:
                instance.save()
        except Exception, e:
            instance.user=request.user
            instance.save()
        
        return instance



admin.site.register(Nota, NotaAdmin)
admin.site.register(Severidad_nota,SeverityAdmin)
