num1=int(input("ingrese su primer numero "))
num2=int(input("ingrese su segundo numero "))
num3=int(input("ingrese su tercero numero "))
if (num1 + num2) == num3:
    print ("La suma entre numero 1 y numero 2 es el numero 3")
elif  (num2 + num3) == num1:
    print ("La suma entre numero 2 y numero 3 es el numero 1")
elif (num1 + num3) == num2:
    print ("La suma entre numero 1 y numero 3 es el numero 2")
else: print("ninguno es la suma del otro")