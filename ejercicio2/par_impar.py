#---pedimos el numero y la potencia al usuario---
num=int(input("ingrese un numero: "))
pot = int(input("Ingrese la potencia: "))
#---sacamos el resultado---
res=num**pot
#---sacamos si el resultado es par o impar
if res % 2 == 0:
	print("El resultado es par")
else:
	print("El resultado es impar")