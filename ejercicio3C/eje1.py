'''Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular la nota media de cada estudiante y la nota media de la clase al
completo.
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
clase. '''
lNombres=['Juan','Lautaro','Martina','Bautista','Walter','Ramiro','Natalia','Martha']
lNotas=[[4.0, 4.0, 4.0], [10.0, 10.0, 10.0], [6.0, 7.0, 4.0], [5.0, 3.33, 9.5], [9.99, 5.66, 7.0], [1.1, 1.1, 1.1], [4.0, 4.0, 4.0], [10.0, 5.0, 9.0]]
lMedia=[]
total=0
for i in lNotas:
	suma=0
  prom=0
	for num in range(0,3):
  	suma+=i[num]
	prom=suma/3
  lMedia.append(prom)

for i in lMedia:
	total+=i
print(lMedia)
print('el promedio total es', {total})