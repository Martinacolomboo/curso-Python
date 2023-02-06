lista1=list(range(1,20))
lista2=[2,30,7,98,15]
lista=[]
for i in lista1:
    if i in lista2:
        lista.append(i)
print(lista)