from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Categoria en las que se pueden agrupar los sitemas o dispositivos hardware o software
class Categoria(models.Model):
    name = models.CharField('Nombre',max_length=50,unique=True)
    description = models.TextField('Descripcion',max_length=120, help_text='Descripcion breve sobre la categoria')
    imagen =  models.ImageField( upload_to='sistemas/categorias',null=True, default= 'sistemas/categorias/default.png',help_text='Campo Opcional')
    is_active = models.BooleanField('Activo',default=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='creado el')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='actualizado el')
    user = models.ForeignKey(User)

    class Meta:
        #db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'

    def __unicode__(self):
        return self.name

    def creado_por(self):
        return "%s %s" % (self.user.first_name, self.user.last_name,)



#Ubicacion fisica en donde se encuentran los sistemas o subsistemas
class Ubicacion(models.Model):
    name = models.CharField('Nombre',max_length=50,unique=True)
    description = models.TextField('Descripcion',max_length=120, help_text='Descripcion breve sobre la ubicacion')
    is_active = models.BooleanField('Activo',default=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='creado el')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='actualizado el')
    user = models.ForeignKey(User,
         verbose_name='Creado por',)
    #parent = models.ForeignKey('self',
       # verbose_name='Ubicacion padre',null=True, blank=True)

    class Meta:
        #db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Ubicaciones'
        verbose_name = 'Ubicacion'

    def __unicode__(self):
        return self.name
    
    def creado_por(self):
        return "%s %s" % (self.user.first_name, self.user.last_name,)


 #Sistemas que se usan en EAAI
class Sistema(models.Model):
    SYS_TYPE_CHOICES = (
        ('SW', 'SOFTWARE'),
        ('HW', 'HARDWARE'),
        ('OTRO', 'OTRO'),
    )
    name = models.CharField('Nombre',max_length=50, )
    short_name=models.CharField('Nombre Pos. (Siglas)',max_length=20,unique=True, default="", blank=False)
    description = models.TextField('Descripcion',max_length=120, help_text='Descripcion breve sobre el sistema')
    sys_type = models.CharField('Tipo de sistema',choices=SYS_TYPE_CHOICES, max_length=30)
    is_active = models.BooleanField('Activo',default=True)
    en_funcionamiento=models.BooleanField(default=True)
    ubication = models.ForeignKey(Ubicacion, verbose_name='Ubicacion')
    category = models.ForeignKey(Categoria, verbose_name='Categoria')
    imagen =  models.ImageField( upload_to='sistemas/sistemas', null=True, default= 'sistemas/sistemas/default.png',help_text='Campo Opcional')
    #parent = models.ForeignKey('self', verbose_name=u'Sistema Padre', null=True, blank=True,help_text='Campo Opcional')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='creado el')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='actualizado el')
    user = models.ForeignKey(User, 
        verbose_name='Creado por',)
    
    class Meta:
         #db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Sistemas'
        verbose_name = 'Sistema'

    def __unicode__(self):
        return self.short_name
    
    def creado_por(self):
        return "%s %s" % (self.user.first_name, self.user.last_name,)



