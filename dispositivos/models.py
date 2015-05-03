from django.db import models
from django.contrib.auth. models import User
from sistemas.models import Ubicacion
from django.dispatch import receiver
import os

# Create your models here.

#1===============================================================================================
class Tipo_Dispositivo(models.Model):
    nombre= models.CharField(max_length=30,)
    activo= models.BooleanField("Activo",default=True)
    imagen =  models.ImageField( upload_to='dispositivos/tipo_dispositivo', null=True, default= 'dispositivos/tipo_dispositivo/default.png',help_text='Campo Opcional')
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    usuario = models.ForeignKey(User, verbose_name='Creado por',)
    
    class Meta:
        verbose_name_plural = 'Tipos de Dispositivo'
        verbose_name = 'Tipo de Dispositivo'
        
    def __unicode__(self):
        return self.nombre

#2===============================================================================================
class Dispositivo(models.Model):
    TIPO_OS = (
        ('WINDOWS', 'Windows'),
        ('RHE', 'Red Hat'),
        ('CentOS', 'Cent OS'),
        ('Debian', 'Debian'),
        ('Solaris', 'Solaris'),
        ('CISCO', 'Cisco IOS'),
        ('OTRO', 'Otro'),
        ('N/A', 'No Aplica'),
    )
    TIPO_ESTADO = (
        ('FUNCIONAL', 'Funcional'),
        ('SEMIFUNCIONAL', 'Semifuncional'),
        ('FALLO', 'Fallo'),
    )
    nombre= models.CharField(max_length=30, unique=True)
    os = models.CharField('Sistema Operativo',choices=TIPO_OS, max_length=30,)
    marca = models.CharField("Marca", max_length=30,default="Sin Especificar")
    modelo = models.CharField("Modelo", max_length=30,default="Sin Especificar")
    serie = models.CharField("Numero de Serie", max_length=40, unique=True)
    inventario = models.CharField("Numero de Inventario", max_length=40, unique=True,null=True)
    ip=models.IPAddressField("Direccion IP", max_length=15,blank=True,default="0.0.0.0")
    mascara_red=models.CharField("Mascara IP", max_length=15,blank=True,default="N/A")
    descripcion = models.TextField('Descripcion',max_length=160, help_text='Descripcion del dispositivo',blank=True,default="Sin Especificar")
    ubicacion= models.CharField(max_length=30,help_text='Indica la ubicacion fisica')
    tipo=models.ForeignKey(Tipo_Dispositivo)
    estado=models.CharField(choices=TIPO_ESTADO, max_length=30,)
    activo= models.BooleanField("Activo",default=True)
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    usuario = models.ForeignKey(User, verbose_name='Creado por',)

    class Meta:
        verbose_name_plural = 'Dispositivos'
        verbose_name = 'Dispositivo'
        
    def __unicode__(self):
        return self.nombre

#3===============================================================================================
class Tipo_Componente(models.Model):
    nombre= models.CharField(max_length=30,)
    activo= models.BooleanField("Activo",default=True)
    imagen =  models.ImageField( upload_to='dispositivos/componente', null=True, default= 'dispositivos/componente/default.png',help_text='Campo Opcional')
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    usuario = models.ForeignKey(User, verbose_name='Creado por',)
    
    class Meta:
        verbose_name_plural = 'Tipos de Componente'
        verbose_name = 'Tipo de Componente'
        
    def __unicode__(self):
        return self.nombre
#4===============================================================================================
class Componente_hardware(models.Model):
    dispositivo= models.ForeignKey(Dispositivo,verbose_name='Instalado en',null=True)
    marca = models.CharField("Marca", max_length=30,default="Sin Especificar")
    modelo = models.CharField("Modelo", max_length=30,default="Sin Especificar")
    serie = models.CharField("Numero de Serie", max_length=40,unique=True)
    tipo =models.ForeignKey(Tipo_Componente)
    descripcion = models.TextField('Descripcion',max_length=160, help_text='Descripcion del componente',blank=True)
    activo= models.BooleanField("Activo",default=True)
    operando = models.BooleanField("En funcionemiento",default=True)
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    usuario = models.ForeignKey(User, verbose_name='Creado por',)

    class Meta:
        verbose_name_plural = 'Componentes Hardware'
        verbose_name = 'Componente Hardware'
        
    def __unicode__(self):
        return self.serie

#5===============================================================================================
class Historial_equipo(models.Model):
    TIPO_ENTRADA = (
        ('MANTENIMIENTO', 'Mantenimiento'),
        ('FALLO', 'Fallo'),
    )
    TIPO_ESTADO = (
        ('FUNCIONAL', 'Funcional'),
        ('SEMIFUNCIONAL', 'Semifuncional'),
        ('FALLO', 'Fallo'),
    )
    dispositivo= models.ForeignKey(Dispositivo,)
    tipo_entrada = models.CharField("Entrada por",choices=TIPO_ENTRADA, max_length=30,)
    estado_antes=models.CharField(choices=TIPO_ESTADO, max_length=30,)
    descripcion = models.TextField(max_length=3000, help_text='Descripcion de trabajo',verbose_name='descripcion')
    estado_despues=models.CharField(choices=TIPO_ESTADO, max_length=30,)
    ubicacion_antes= models.CharField(max_length=40,)
    ubicacion_despues= models.CharField(max_length=40,)
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    usuario = models.ForeignKey(User, verbose_name='Creado por',)

    class Meta:
        verbose_name_plural = 'Historial de dispositivos'
        verbose_name = 'Historial'
        ordering = ['-creado']
        
    def __unicode__(self):
        return self.tipo_entrada



