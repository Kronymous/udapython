
lenjuages = ['python', 'kotlin', 'Java', 'JavaScrip']
print(lenjuages)

#Los arrays (lists) comienzan en la posicion cero [0]
print(lenjuages[0]) #python

#Ordenar los elementos
lenjuages.sort()
print(lenjuages)

#Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo{lenjuages[3]}'
print(aprendiendo)

#Modificando valores de un arreglo
lenjuages[2] = 'PHP'   #cambiando java por PHP
print(lenjuages)

#Agregar elementos a un arreglo (list)
lenjuages.append('Ruby')
print(lenjuages)

#Eliminar un elemento de un arreglo (list)
del lenjuages[1]
print(lenjuages)

#Elininar un elemento del arreglo (list)
lenjuages.pop()
print(lenjuages)

#Eliminar un elemento con pop de una pocision en especifico
lenjuages.pop(0)
print(lenjuages)

#Eliminar por nombre
lenjuages.remove('PHP')
print(lenjuages)