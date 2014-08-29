from django.contrib import admin
from usuario.models import *

class PerfilAdmin (admin.ModelAdmin):
    list_display=('id','usuario','cargo','telefono')
    #list_filter=('user__username',)
   # search_fields=('user__username','keywords')
    list_per_page = 10

    #raw_id_fields=('systems',)


admin.site.register(Perfil, PerfilAdmin)