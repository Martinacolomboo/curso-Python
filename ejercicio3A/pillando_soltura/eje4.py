lista=list(range(9,20))
num=int(input("Ingrese  numero "))
cant=0
for i in lista:
    if i>num:
        cant=cant+1
print(cant)