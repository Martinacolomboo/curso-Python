#profe:
# --- Pedimos un numero al usuario ---
numero = input("Por favor, introduce un número de cuatro cifras ") #string

#una manera de hacerlo:
print(numero[::-1])

#otra manera:
# --- Creamos el strig inverso ---
numero_inverso = numero[3] + numero[2] + numero[1] + numero[0]

# --- imprimos el resultado por pantalla
print(numero_inverso)
