from mongoengine import *
from dateutil import parser
import datetime
from datetime import date, timedelta

connect('horario',host='192.168.137.200')
#connect('horario')

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
	ultimo_rol= ReferenceField(MatrizHorario)
	iteracion=IntField()
	ultimo_rolValid= ReferenceField(MatrizHorario)
	iteracionValid=IntField()


class Horario(Document):
	empleado= EmbeddedDocumentField(Empleado)
	fecha_final=DateTimeField()
	semanas=IntField()





def initHorario():
	nombres=["Erick Saenz","Otoniel Saravia","Gabriela Collado","Christian Lopez","Blanca Jarquin","Eveling Moncada","Eder Rojas","Carlos baltodano"]
	matriz=MatrizHorario.objects #obtener la matris de 8 filas correspondiente a cada emp


	i=0

	for nomb in nombres:
		dt = parser.parse("Oct 05 2014 12:00AM")
		emp=Empleado(nombre=nomb,iteracion=1)
		print emp.nombre
		for dia in matriz[i].rol:
			dt = dt+timedelta(days=1)			
			emp.horario_emp.append(Turnos(turno=dia,fecha=dt))
		emp.ultimo_rol=matriz[i]
		emp.iteracion=1
		horario=Horario(empleado=emp,fecha_final=dt,semanas=4)
		horario.save()
		i=i+1

def initHorario2():
	roles=MatrizHorario.objects #obtener la matris de 8 filas correspondiente a cada emp
	for rol in roles:
		rol.tarea="CMD"
		rol.save()



def clearHorario_Emp():
	emps=Horario.objects
	dt = parser.parse("Oct 05 2014 12:00AM")
	for emp in emps:
		emp.empleado.horario_emp=[]
		emp.fecha_final=dt
		emp.save()

def getRolIndex(roles,emp):
	for rol in range(0,roles.count()):
			if emp.empleado.ultimo_rol == roles[rol]:
				return rol

def autoCreateEmp_Horario(weeks):
	roles=MatrizHorario.objects #obtener la matris de 8 filas correspondiente a cada emp
	emps=Horario.objects #obtener la lista de 8 empleados
	
	semanas=13 #simular el rol para 13 semanas en el futuro a partir de la fecha en que termino el rol anterior
	semanas_rol=weeks #numero de semanas que seran efectivas el resto 9 semanas teoricas
	#recorres la lista de 8 emps
	for emp in emps:
		fechaAct=emp.fecha_final #obtener la fecha en que termina el rol
		emp.empleado.iteracion=emp.empleado.iteracionValid
		emp.empleado.ultimo_rol=emp.empleado.ultimo_rolValid
		emp.empleado.horario_emp=[]#Vaciar lista de horario antigua

		#generar el Rol para determinado numero de semanas
		for semana in range(0,semanas):
			##------Averiguar la posicion del ultimo horario del empleado
			rolIndex=getRolIndex(roles,emp)
			#print "El rol del empleado "+emp.empleado.nombre +" es "+rolIndex.__str__()
			if emp.empleado.iteracion < 2:
			#	print "iteracion 1 volver a ejecutar ese rol"
				#agregar los siete dias con el turno correspondiente al elmpleado
				for dia in roles[rolIndex].rol:
					fechaAct=fechaAct+timedelta(days=1)	
					emp.empleado.horario_emp.append(Turnos(turno=dia,fecha=fechaAct,
						tareas=roles[rolIndex].tareas,horas_t=roles[rolIndex].horas_t,total_h=roles[rolIndex].total_h,extras=roles[rolIndex].extras))
				#aumentar la iteracio
				emp.empleado.iteracion=emp.empleado.iteracion+1
				emp.save()
			else:
			#	print "iteracion 2 pasar al siguiente rol"
				if rolIndex<roles.count()-1:
					rolIndex=rolIndex+1
				else:
					rolIndex=0
				for dia in roles[rolIndex].rol:
					fechaAct=fechaAct+timedelta(days=1)	
					emp.empleado.horario_emp.append(Turnos(turno=dia,fecha=fechaAct,
						tareas=roles[rolIndex].tareas,horas_t=roles[rolIndex].horas_t,total_h=roles[rolIndex].total_h,extras=roles[rolIndex].extras))
				emp.empleado.ultimo_rol=roles[rolIndex]
				#aumentar la iteracio
				emp.empleado.iteracion=1
				emp.save()

			if semana==(semanas_rol-1):
				emp.fecha_final= fechaAct
				emp.empleado.iteracionValid=emp.empleado.iteracion
				emp.empleado.ultimo_rolValid=emp.empleado.ultimo_rol
				emp.save()
	

#clearHorario_Emp()
#autoCreateEmp_Horario(4)

#initHorario2()
