'''Define una lista de 5 palabras aleatorias y 
una lista de letras prohibidas que contenga tres 
letras.
Filtra las palabras en tu lista original crea una 
nueva lista de palabras filtradas que solo 
contenga aquellas palabras que no tienen ninguna
 letra prohibida. '''
listaA=['manzana','banana','durazno','anana','uva']
listaP=['m','u','v']
lista=[];
for i in listaA:
	if not(listaP[0] in i) and not(listaP[1] in i) and not(listaP[2] in i):
  	lista.append(i)
print(lista)

