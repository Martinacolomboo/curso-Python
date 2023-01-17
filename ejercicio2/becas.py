#---pedimos la info del usuario---
nom=input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nota = float(input("Ingrese su nota media: "))

if (((edad>=17)and (edad<=21)) and (nota>=8)):
	print(nom.title(),"puede acceder a la beca")
else:
	print (nom.title(), "no puede acceder a la beca")