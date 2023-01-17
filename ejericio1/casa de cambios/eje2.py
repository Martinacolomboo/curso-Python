#ingrese el monto
euros=float(input("ingresar la cantidad de euros: "))
#euros pasados a dolar
dolar=euros*1.2
#sacamos lo q le queda a la casa de cambio
descuento=dolar*0.10
#sacamos lo q le queda al ususario
usuario= dolar-descuento
#imprimimos
print("El monto recibidio en euros es: ",euros )
print("El cambio a dolar: ",dolar)
print("La cantidad q se queda la casa de cambio es: ",descuento)
print("La cantidad q se queda el usuario es: ",usuario)