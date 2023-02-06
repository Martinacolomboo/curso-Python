lista=list(range(1,101))
num=int(input("Ingrese un numero "))
suma=0
for i in lista:
    if (i % num )== 0:
        suma=suma+i
print(suma)