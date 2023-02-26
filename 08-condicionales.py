'''

#Revisar si una condicion es mayor a
balance = 500
if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')

#Likes
likes = 200
if likes >= 200:
    print ('Excelente, 200 likes')
else:
    print('Casi llegas a los 200 likes')

#IF con texto
lenguaje = 'PHP'
if not lenguaje =='Python':
    print('Excelente decision')

#Evaluar un Boleano
usuario_autenticado = True

if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')

'''

#if anidados
usurio_autenticado = False
usuario_admin = False

if usurio_autenticado:
    if usuario_admin:
        print('Acceso Total')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesion')