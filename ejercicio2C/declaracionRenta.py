edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese cuanto cobra: "))

if edad >= 18 and sueldo > 1000:
    if sueldo < 15000:
        tipo = 5
    elif 15000 <= sueldo < 25000:
        tipo = 15
    elif 2500 <= sueldo < 35000:
        tipo = 20
    elif 35000 <= sueldo < 60000:
        tipo = 30
    else:
        tipo = 45
    print("Sos susceptible, te corresponde un",tipo,"%")
else:
    print("No sos susceptible")

