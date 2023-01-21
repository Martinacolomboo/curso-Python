long1=float(input("Ingrese la primera longitud "))
long2=float(input("Ingrese la segunda longitud "))
long3=float(input("Ingrese la tercera longitud "))
if (long1+long2>long3) and (long2+long3>long1) and (long1+long3>long2):
    print("Se puede construir la estructura")
else: print ("No se puede contruir la estructura")