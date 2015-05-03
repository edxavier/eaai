db.horario.drop()

db.horario.save({
	empleado:{
		nombre:"Eder Rojas",
		horario_emp:[{turno:"T1",fecha:"01/01/2014"},{turno:"T1",fecha:"02/01/2014"},{turno:"T1",fecha:"03/01/2014"}],
		ultimo_rol:1,
		iteracion:1
	},
	fecha_final:"04/01/2014",
	semanas:4
})