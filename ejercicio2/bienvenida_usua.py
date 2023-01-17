#--- Pedimos el nombre del usuario--
nom= input("ingrese su nombre: ")
#--- Declaramos los nombres ---
usua1="namomi"
usua2="alejandro"
usua3="sergio"
#--- Le sacamos los puntos y las almohadillas ---
nom = nom.replace(".","")
nom = nom.replace("#","")
#--- Preguntamos que usuario es ---
if nom.lower() == usua1:
	print("Hola,", usua1.title())
elif nom.lower() == usua2:
	print("Hola,", usua2.title())
elif nom.lower() == usua3:
	print("Hola,", usua3.title())
else:
	print("Hola, usuario invitado")