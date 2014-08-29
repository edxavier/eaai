from django.forms import ModelForm, TextInput, DateTimeInput
from django.contrib.admin import ModelAdmin
from bitacora.models import  Nota, Severidad_nota
from suit.widgets import EnclosedInput, LinkedSelect
from suit.widgets import EnclosedInput
from suit_redactor.widgets import RedactorWidget
from django_select2.widgets import Select2MultipleWidget, Select2Widget



class NotaForm(ModelForm):
    class Meta:
        model = Nota
        exclude=('user',)
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'es'}),
            'referencia': Select2Widget(select2_options={
                'minimumResultsForSearch': 1,
                'closeOnSelect': True,
                'width':200
                }),
            'severity': Select2Widget(select2_options={
                'minimumResultsForSearch': 1,
                'closeOnSelect': True,
                'width':200
                })
        }


class EstadoForm(ModelForm):
    class Meta:
        model = Severidad_nota
        exclude=('user',)

class NotaForm2(ModelForm):
    class Meta:
        model = Nota
        exclude=('user',)
        widgets = {
            'keywords': TextInput(attrs={'placeholder': "Palabras clave delimitadas por coma"}),
        }
        
