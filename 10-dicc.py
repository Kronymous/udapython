#creando un diccionario simple
cancion = {
    'artista' : 'metalica', #llave y valor
    'cancion' : 'Enter sandman',
    'Lanzamiento' : 1992,
    'Likes' : 3000
}
#Acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['cancion'])
print(cancion['Lanzamiento'])
print(cancion['Likes'])

#mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')
print(cancion)

#agregar una vueva llave llamada playlist
cancion['playlist'] = 'Heavy Metal'
print(cancion)

#remplazar valor existente
cancion['cancion'] = 'seek & destroy'
print(cancion)

#eliminar un valor
del cancion['Lanzamiento']
print(cancion)