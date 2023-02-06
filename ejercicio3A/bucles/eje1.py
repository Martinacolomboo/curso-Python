num = int(input("ingrese un numero entero: "))
a = ""
for i in range(0,num):
	a = a + "*"
	print(a)

for i in range(0,num):
	num=num-1
	print(a[0:num])