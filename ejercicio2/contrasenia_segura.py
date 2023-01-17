#--- Pedimos la contraseña del usuario--
con = input("ingrese su contraseña: ")

#--- nos fijamos si la contra cumple las condiciones para ser segura ---
if  (("a" in con) or ("e" in con)or ("i" in con)or ("o" in con)or ("u" in con)) and (("*" in con) and ("#" in con)): 
	print("La constraseña ingresada es segura")
else:
	print("La constraseña ingresada no es segura")