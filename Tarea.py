#Funciones: Me imprime el nombre de la universidad y el nombre del alumno
def uda():
      nombre = 'Miguel Angel'
      print('UNIVERSIDAD DEL ATLANTICO')
      print('Hola ' + nombre)
uda()
print('-------------------------------------------------------------------')
#condicionales: Si el alumno no a pagado tiene falta
alumno = 'Miguel angel'
pagos = False
if pagos:
    print('Tienes todo pagado y no tienes faltas')
else:
    print('Tienes una falta por adeudo, ponte al corriente')
#Muestra si el alumno tiene 3 faltas esta reprobado
faltas = 3
if faltas >=3:
    print('Juntaste 3 faltas y estas reprobado')
else:
    print('Atenciontienes 2 faltas, puedes reprobar')
#Si el promedio del alumno es menor a 8 esta reprobado si es mayor a 8 esta aprobado
promedio = 6
if promedio >= 7:
    print("Aprobado")
else:
    print(alumno, "Tu calificacion final fue menor a 7 estas reprobado")

print('-------------------------------------------------------------------')
print('ESTAS SON LAS FECHAS Y MATERIAS DE TUS EXTRAORDINARIOS A PRESENTAR')
#FUNCION
def extraordinario(materia, fecha):
        print(f'{materia} , {fecha}')

extraordinario('Matematicas','30/02/2023')
extraordinario('Ingles','05/03/2023')
extraordinario('Programacion','10/03/2023')
extraordinario('Base de datos','15/03/2023')

