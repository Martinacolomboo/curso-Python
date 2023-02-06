lista=list(range(1,10))
num=int(input("Ingrese un numero "))
i=0
actual=lista[i]
while actual != num :
    anterior=actual
    i+=1
    actual=lista[i]
print(anterior)