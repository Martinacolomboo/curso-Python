#--pedimos la contra al usuario--
con = input("Ingrese la contraseña: ")
contra_segura= "contrase"
#---comprobamos si es correcta--
if (con.lower()== contra_segura):
	print("Bienvenido")
else:
    print("La contra es incorrecta")
    con= input("Ingrese la contraseña: ")	
    if (con.lower()== contra_segura):
	    print("Bienvenido")
    else:
  	    print("Error")   