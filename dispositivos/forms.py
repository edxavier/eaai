from django.forms import ModelForm, TextInput, DateTimeInput
from .models import  *
from suit.widgets import EnclosedInput, LinkedSelect
from suit.widgets import EnclosedInput
from suit_redactor.widgets import RedactorWidget
from django_select2.widgets import Select2MultipleWidget, Select2Widget



class Historial_Form(ModelForm):
    class Meta:
        model = Historial_equipo
        exclude=('usuario',)
        

class Dispositivo_Form(ModelForm):
    class Meta:
        model = Dispositivo
        exclude=('usuario',)

class Historial_equipo_AdminFRM(ModelForm):
    class Meta:
        model = Historial_equipo
        exclude=('usuario',)
        widgets = {
            'descripcion': RedactorWidget(editor_options={'lang': 'es'}),
            'dispositivo': Select2Widget(select2_options={
                'minimumResultsForSearch': 1,
                'closeOnSelect': True,
                'width':200
                }),
        }

class DispositivoAdminFRM(ModelForm):
    class Meta:
        model = Dispositivo
        exclude=('usuario',)
        widgets = {
            'descripcion': RedactorWidget(editor_options={'lang': 'es'}),
            'dispositivo': Select2Widget(select2_options={
                'minimumResultsForSearch': 1,
                'closeOnSelect': True,
                'width':200
                }),
        }