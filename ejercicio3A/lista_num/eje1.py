num=[1,2,3,4,5,6,7,8,9,10]

pares = []

for numero in num:
	if ((numero % 2) == 0):
  	    pares.append(numero)
pares.reverse()
print(pares)
for valor in num:
	print(valor**2)
#se le agrega a pares de otra forma
for numero in range(-1,-11,-1):
    if ((num[numero] % 2) == 0):
  	    pares.append(num[numero])
print(pares)
print(min(num))
print(max(num))
print(sum(num))
valor=0
for suma in num:
	valor=valor+suma
print(valor)

numero = 0
while (num[numero] != 8):
	numero = numero + 1
print(numero)
numero = 0
while (pares[numero] != 8):
	numero = numero + 1
print(numero)