from django.db import models
from django.contrib.auth.models import User
from sistemas.models import *
# Create your models here.
from django.dispatch import receiver



class Severidad_nota(models.Model):
    name = models.CharField('Nombre',max_length=50,unique=True, )
    description = models.TextField('Descripcion',max_length=120, help_text='Descripcion breve sobre el sistema')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='creado el')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='actualizado el')
    user = models.ForeignKey(User, 
        verbose_name='Creado por',)

    class Meta:
         #db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Niveles de Severidad'
        verbose_name = 'Nivel de Severidad'

    def __unicode__(self):
        return self.name
    
    def creado_por(self):
        return "%s %s" % (self.user.first_name, self.user.last_name,)





class Nota(models.Model):
    severity = models.ForeignKey(Severidad_nota, verbose_name='Estado ',)
    systems = models.ManyToManyField(Sistema, blank=True,verbose_name='Sistemas')
    description = models.TextField(max_length=3000, help_text='Descripcion de la nota',verbose_name='descripcion')
    keywords= models.CharField(max_length=150, help_text='(Opcional) Palabras clave delimitadas por coma',blank=True,)
    referencia = models.ForeignKey('self', verbose_name=u'Referencia a nota', null=True, blank=True,help_text='Campo Opcional')
    adjuntos= models.FileField(upload_to='nota/adjuntos',blank=True,null=True,help_text='Campo Opcional')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='creado el')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='actualizado el')
    user = models.ForeignKey(User, 
        verbose_name='Creado por',)

    class Meta:
         #db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Notas'
        verbose_name = 'Nota'

    def __unicode__(self):
        return  "Nota: %d" % (self.pk, )
    
    def creado_por(self):
        return "%s %s" % (self.user.first_name, self.user.last_name,)
        
    def sistemas_involucrados(self):
        return "%d" % (self.systems.count(),)
