from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import os

class Perfil(models.Model):
    usuario = models.OneToOneField(User)
    foto = models.ImageField( upload_to='perfiles',null=True, default= 'perfiles/default.jpg')
    cargo= models.CharField(max_length=100, blank=True)
    telefono= models.CharField(max_length=15, blank=True)
    fecha_nacimiento= models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Perfiles'
        verbose_name = 'Perfil'
        
    def __unicode__(self):
        return self.usuario.username 


#esta funcion va fuera de la clase y es para eliminar un archivo cuando se actualiza el campo
@receiver(models.signals.pre_save, sender=Perfil)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
        when corresponding `MediaFile` object is changed.
    """
    #si no existe el objeto no hagas nada y salvalo normal
    if not instance.pk:
        return False
    #intenta darme el archivo anterior
    try:
        old_file = Perfil.objects.get(pk=instance.pk).foto
    except Perfil.DoesNotExist:
        return 

    if os.path.basename(old_file.path) == "default.jpg":
        return False
    #dame el archivo q viene en el objeto a actualizar
    new_file = instance.foto
    #si no son los mismos archivos elimina el anterior
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)




User.perfil = property (lambda u: Perfil.objects.get_or_create(usuario=u)[0])