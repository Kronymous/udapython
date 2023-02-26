#Ejemplo de condional OR

usuario_logueado = True
usuario_admin = True

if usuario_logueado or usuario_admin:
    print('Administrador')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')

#Ejemplo de condicional AND

usuario_logueado = True
usuario_admin = True

if usuario_logueado and usuario_admin:
    print('Administrador')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')