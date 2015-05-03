from mongoengine import *
#connect('horario',host='192.168.137.200')
connect('horario')

# Create your models here.
class Turnos(EmbeddedDocument):
	turno = StringField(required=True)
	fecha = DateTimeField()
	total_h=IntField()
	horas_t=IntField()
	extras=IntField()
	tareas=StringField()

class MatrizHorario(Document):
	rol = ListField(StringField(max_length=3))
	repeticiones= IntField()
	tareas=StringField()
	total_h=IntField()
	horas_t=IntField()
	extras=IntField()


class Empleado(EmbeddedDocument):
	nombre = StringField()
	horario_emp=ListField(EmbeddedDocumentField(Turnos))
	tareas=StringField()
	ultimo_rol= ReferenceField(MatrizHorario)
	iteracion=IntField()
	ultimo_rolValid= ReferenceField(MatrizHorario)
	iteracionValid=IntField()

class Horario(Document):
	empleado= EmbeddedDocumentField(Empleado)
	fecha_final=DateTimeField()
	semanas=IntField()

