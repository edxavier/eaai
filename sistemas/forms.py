from django.forms import ModelForm, TextInput, DateTimeInput
from django.contrib.admin import ModelAdmin
from sistemas.models import *
from suit.widgets import EnclosedInput, LinkedSelect
from suit.widgets import EnclosedInput
from django_select2.widgets import Select2MultipleWidget, Select2Widget


class SistemaForm(ModelForm):
	class Meta:
		model = Sistema
		exclude=('user',)
		widgets = {
            'ubication': Select2Widget(select2_options={
                'minimumResultsForSearch': 1,
                'closeOnSelect': True,
                'width':200
                }),
            'category': Select2Widget(select2_options={
                'minimumResultsForSearch': 1,
                'closeOnSelect': True,
                'width':200
                })
        }

class UbicacionForm(ModelForm):
    class Meta:
        model = Ubicacion
        exclude=('user',)

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        exclude=('user',)