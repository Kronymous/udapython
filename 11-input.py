'''
nombre = input('Cual es tu nombre: \r\n') #tiene salto de linea

print(f'Hola {nombre}')

#leer datos que seran numeros
edad = int (input('Cual es tu edad?: '))

if edad >=18:
    print('ya puedes votar')
else:
    print('aun no puedes votar')

#mezclarlo con operadores
numero = int (input('agregar un numero y te dire si es par o  impar: '))

if numero % 2 == 0:
    print(f'El numero es {numero} es par')
else:
    print(f'El numero {numero} es impar')
'''
'''
Realiza un examen con 3 preguntas que tu deses, el usuario  debera responder 'si' o 'no'  y al final
otorgarle una calificacion (la calificacion se logra con una variable que inicia en 0 y por cada respuesta incrementa 1
'''

print("¡Bienvenido al examen!")
puntuacion = 0

preguntas = [
    "¿Has viajado fuera de tu país de origen alguna vez?",
    "¿Te gusta cocinar?",
    "¿Has leído al menos un libro en el último mes?",
]

for pregunta in preguntas:
    respuesta = input(f"{pregunta} (si/no):  ")
    if respuesta.lower() == "si":
        puntuacion += 1

print(f"Tu puntuación final es: {puntuacion}/{len(preguntas)}")












