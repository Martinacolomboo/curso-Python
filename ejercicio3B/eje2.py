'''Dado una lista de números enteros, escribe un 
script en Python que devuelva una nueva lista con
los números primos de la lista original. Además, 
el script debe devolver el número total de
números primos encontrados y la suma de los 
números primos encontrados'''

lista=[20, 17, 9, 7, 54]
listaP=[]
total=0
suma=0
for num in lista:
    primo = True
    i = 2
    while primo == True and i < num:
        if num % i == 0:
            primo = False
        i += 1
    if primo:
        listaP.append(num)
        suma=suma+num
        total+=1
print(listaP)
print(suma)
print(total)