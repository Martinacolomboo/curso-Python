precio=float(input("Ingrese el precio "))
if (precio<100):
    print ("La orden de compra")
elif (precio>=100)and (precio<=150):
    print("La orden de hold")
else:
    print("La orden de vender")