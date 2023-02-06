#eje1
frutas = ['manzana','platano','cereza','pera','higo','frambuesa','fresa']
#eje2
print(len(frutas))
#eje3
print(frutas[3])
#eje4
frutas[2] = 'mora'
#eje5
frutas.append('mango')
#eje6
frutas.insert(0,'uva')
#eje7
for fruta in frutas:
	print(fruta)
#eje8
ultima_fruta = frutas.pop()
print(frutas)
#eje10
for fruta in frutas:
	print(fruta, len(fruta))
#eje11
for fruta in frutas:
	 if (len(fruta) >= 5):
   	    print(fruta)
#eje12
frutas.remove('higo')
print(frutas)
#eje13
frutas.clear()
print(frutas)