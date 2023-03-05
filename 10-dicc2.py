#iniciar un diccionario basio
jugador = {}
print(jugador)

#se une un jugador
jugador['nombre'] = 'Juan'
jugador['puntuaje'] = 0
print(jugador)

#incrementando en el puntuaje
jugador['puntuaje'] = 100
print(jugador)

#incrementando en el puntuaje
jugador['puntuaje'] = 200
print(jugador)

#acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))

#iterar en el diccionario
for llave, valor in jugador.items():
    print(valor)

#eliminar jugador y puntuaje
del jugador['nombre']
del jugador['puntuaje']
print(jugador)
