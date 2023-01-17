#---pedimos dos numeros al usuario---
num1=int(input("Ingrese un numero "))
num2=int(input("Ingrese otro numero "))
#---nos fijamos si el divisor es 0, si es asi imprime error
if (num2==0):
	print("Error")
#--- si no la division
else:
	print(int(num1/num2))