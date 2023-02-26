#Ejemplo con elif
ocupacion = 'desempleado'

if ocupacion == 'Estudiante':
    print('Tienes 50% de descuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de descuento')
elif ocupacion == 'desempleado':
    print('Tines un 10% de descuento')
else:
    print('Debes pagar el 100%')

