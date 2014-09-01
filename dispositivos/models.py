from django.db import models
from django.contrib.auth. models import User
from sistemas.models import Ubicacion
from django.dispatch import receiver
import os

# Create your models here.
#0===============================================================================================
class Servicio(models.Model):
    nombre= models.CharField(max_length=30,)
    activo= models.BooleanField("Activo",default=True)
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
    usuario = models.ForeignKey(User, verbose_name='Creado por',)

    class Meta:
        verbose_name_plural = 'Servicios'
        verbose_name = 'Servicio'
        
    def __unicode__(self):
        return self.nombre 
    
#1===============================================================================================
class Tipo_Dispositivo(models.Model):
    nombre= models.CharField(max_length=30,)
    activo= models.BooleanField("Activo",default=True)
    imagen =  models.ImageField( upload_to='dispositivos/tipo_dispositivo', null=True, default= 'dispositivos/tipo_dispositivo/default.png',help_text='Campo Opcional')
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
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
    nombre= models.CharField(max_length=30,)
    os = models.CharField('Sistema Operativo',choices=TIPO_OS, max_length=30,)
    servicios= models.ManyToManyField(Servicio, blank=True,verbose_name='Servicios')
    marca = models.CharField("Marca", max_length=30,default="S/E")
    modelo = models.CharField("Modelo", max_length=30,default="S/E")
    serie = models.CharField("Numero de Serie", max_length=40, unique=True)
    ip=models.CharField("Direccion IP", max_length=15,blank=True,default="N/A")
    mascara_red=models.CharField("Mascara IP", max_length=15,blank=True,default="N/A")
    descripcion = models.TextField('Descripcion',max_length=160, help_text='Descripcion del dispositivo',blank=True,default="S/E")
    ubicacion= models.ForeignKey(Ubicacion)
    tipo=models.ForeignKey(Tipo_Dispositivo)
    operando = models.BooleanField("En Buen Estado",default=True)
    activo= models.BooleanField("Activo",default=True)
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
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
    imagen =  models.ImageField( upload_to='dispositivos/tipo_dispositivo', null=True, default= 'dispositivos/tipo_componente/default.png',help_text='Campo Opcional')
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
    usuario = models.ForeignKey(User, verbose_name='Creado por',)
    
    class Meta:
        verbose_name_plural = 'Tipos de Componente'
        verbose_name = 'Tipo de Componente'
        
    def __unicode__(self):
        return self.nombre
#4===============================================================================================
class Componente_hardware(models.Model):
    dispositivo= models.ForeignKey(Dispositivo,verbose_name='Instalado en',)
    marca = models.CharField("Marca", max_length=30,default="S/E")
    modelo = models.CharField("Modelo", max_length=30,default="S/E")
    serie = models.CharField("Numero de Serie", max_length=40,unique=True)
    tipo =models.ForeignKey(Tipo_Componente)
    descripcion = models.TextField('Descripcion',max_length=160, help_text='Descripcion del componente',blank=True)
    activo= models.BooleanField("Activo",default=True)
    operando = models.BooleanField("En funcionemiento",default=True)
    creado = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    actualizado = models.DateTimeField(auto_now=True,verbose_name='actualizado')
    usuario = models.ForeignKey(User, verbose_name='Creado por',)

    class Meta:
        verbose_name_plural = 'Componentes Hardware'
        verbose_name = 'Componente Hardware'
        
    def __unicode__(self):
        return self.serie



