'''Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios
a un sitio web. Crea un script que verifique si el nombre de usuario y la contraseña ingresados son
correctos y permita el acceso solo si ambos son correctos.
Pista 1: Puedes crear dos listas, una con los nombre de usuario como por ejemplo…
nombres_usuario = ["Nati123", "ana456", "Marta789"]
Y otra lista con las contraseñas guardadas para cada usuario…
contraseñas = ["clave123", "clave456", „clave789"]
Otra opción puede ser que crees una lista de listas con la forma:
nombres_contraseñas = [ ["juan123“,"clave123"] , ["ana456“,“clave456“] , ["Marta789",
"clave789“] ]
Despues puedes pedir el usuario y contraseña y comprobar si coinciden.
Pista 2: Para verificar si el usuario y contraseña son correctos puedes crear un bucle donde
recorras los nombres de usuario y compruebes con un if si el nombre de usuario introducido y la
contraseña coinciden con los datos de tus listas. '''
nombres_contraseñ= [ ['Nati123','clave123'] , ['ana456“,“clave456'] , ['Marta789','clave789'] ]
usuario=input("Ingrese su nombre de usuario: ")
contra=input("Ingrese su contraseña: ")
ok=False
i=0
while not(ok) and i<3:
    if nombres_contraseñ[i][0].title()==usuario.title() and nombres_contraseñ[i][1].title()==contra.title():
  	    ok=True 
    i+=1
if (ok):
    print('Cuenta valida')
else:
    print('Cuenta no valida')