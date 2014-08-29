from django.forms import ModelForm
from usuario.models import Perfil

class PerfilForm(ModelForm):
	class Meta:
		model= Perfil
		exclude = ['usuario']