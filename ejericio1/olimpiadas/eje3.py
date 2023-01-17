minutos = int(input("ingrese la cantidad de minutos: "))
segundo= int(input("ingrese los segundos: "))
centesimas= int(input("ingrese las centesimas: "))
totalmin= minutos*60
totalcen=centesimas*0.01
totalseg= totalmin+totalcen+segundo
metrosporseg=100/totalseg
print("Los metros por segundo son de ", metrosporseg)