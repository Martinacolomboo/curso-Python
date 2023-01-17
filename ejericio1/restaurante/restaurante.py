ensalada = int(input("ingrese la cantidad de ensalada: "))
sopa = int(input("ingrese la cantidad de sopa: "))
dorada = int(input("ingrese la cantidad de dorada al horno: "))
arroz = int(input("ingrese la cantidad de arroz: "))
lasaña = int(input("ingrese la cantidad de lasaña: "))
brownie = int(input("ingrese la cantidad de brownie: "))
helado = int(input("ingrese la cantidad de helado: "))
refresco = int(input("ingrese la cantidad de refresco: "))
cafe = int(input("ingrese la cantidad de cafe: "))

ensaladas = ensalada * 12
sopas = sopa * 10
doradas = dorada * 18
arroces = arroz * 14
lasañas = lasaña * 15
brownies = brownie * 8
helados = helado * 6
refrescos = refresco * 5.5
cafes = cafe * 3.5

print(ensaladas + sopas + doradas + arroces + lasañas + brownies + helados + refrescos + cafes)