'''Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un
programa para realizar un seguimiento de los productos que has vendido y el valor total de las
ventas. Supongamos que hay un total de 10 productos.
Tú has vendido 5 de estos productos en las siguientes cantidades:
Producto 1: 3 unidades
Producto 2: 1 unidad
Producto 5: 7 unidades
Producto 6: 2 unidades
Producto 9 : 4 unidades
Los precios de cada uno de estos productos son como siguen:
Producto 1: 30.0 EU	 	 Producto 6: 44.0 EU
Producto 2: 9.8 EU	 	 Producto 7: 21.2 EU
Producto 3: 42.5 EU	 	 Producto 8: 53.2 EU
Producto 4: 32.6 EU	 	 Producto 9: 25.3 EU
Producto 5: 71.5 EU	 	 Producto 10: 57.8 EU
Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima
la cantidad total de ventas, el dinero facturado por producto y el dinero total. '''
prod=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[20,30,50,18,7,2,23,6,12,11], [30.0, 9.8,42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]]
cant=0
total=0
for num in range(0,len(prod[0])):
	dinero=0
	cant+= prod[1][num]
  dinero= prod[1][num]*prod[2][num]
	print('El dinero facturado por producto ',prod[0][num],' es ',dinero)
  total+=dinero
print(cant)
print(total)
