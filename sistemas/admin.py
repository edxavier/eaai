from django.contrib import admin
from .models import *
from .forms import *



class CategoryAdmin (admin.ModelAdmin):
    list_display=('name','description','user','created_at', 'updated_at',)
    list_filter=('name',)
    search_fields=('categoria__name',)
    list_display_links = ('name',)
    list_per_page = 10
    ordering = ['name']
    #generar el campo slug automaticamente
    #agrupacion por fechas
    date_hierarchy = 'created_at'
#    readonly_fields = ('slug',)
    form=CategoriaForm
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

class PlaceAdmin (admin.ModelAdmin):
    list_display=('name','description','user','created_at', 'updated_at',)
    #list_filter=('user__username',)
    search_fields=('user__username','name','description')
    list_display_links = ('name',)
    list_per_page = 10
    ordering = ['name']
    #prepopulated_fields = {'slug' : ('name',)}
    date_hierarchy = 'created_at'
    form=UbicacionForm
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


class SystemAdmin (admin.ModelAdmin):
    list_display=('name','description','is_active','ubication','category','created_at', 'updated_at','user',)
    list_filter=('user__username',)
    search_fields=('user__username','name','description')
    #presentar radio butons en lugar de select box
    radio_fields = {"sys_type": admin.HORIZONTAL}
    list_display_links = ('name',)
    list_per_page = 10
    ordering = ['-created_at']
    #prepopulated_fields = {'slug' : ('name',)}
    date_hierarchy = 'created_at'
   # list_editable=('ubication', 'category',)
    #raw_id_fields=('ubication',)
    """fieldsets = (
        ('Datos Generales', {
            'fields': ('name', 'slug', 'description', )
        }),
        ('Datos especificos', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('category', 'ubication', )
        }),
    )"""
    form = SistemaForm

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


admin.site.register(Categoria,CategoryAdmin)
admin.site.register(Ubicacion,PlaceAdmin)
admin.site.register(Sistema,SystemAdmin)