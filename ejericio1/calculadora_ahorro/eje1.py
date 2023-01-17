#---- Pedimos el nombre ---
nombre = input("Ingrese su nombre: ")
saludo= "Hola "+ nombre.title()
print(saludo)
#---Plata ganada por hora y horas trabajadas por semana---
plata = float(input("Ingrese su dinero ganado por hora: "))
horas =int(input("Ingrese las horas trabajadas por semana: "))
#---Calculamos el salario semanal, mensual y anual
salario_sem = plata * horas
salario_mes = salario_sem * 4
salario_anual = salario_mes * 12
#---Imprimimos por pantalla el salario anual---
print(nombre.title(), "tiene unas ganancias anuales de:",salario_anual,"euros")
#---Pedimos los gastos semanales---
gastos_sem = float(input("Ingrese los gastos semanales: "))
#---Calculamos los gastos mensuales y anuales---
gastos_mes = gastos_sem * 4
gastos_anuales = gastos_mes * 12
#---Calculamos el ahorro anual---
ahorros_anuales = salario_anual - gastos_anuales
#---Imprimimos por pantalla los gastos y el ahorro anual---
print(nombre.title(), "tiene unos gastos anuales de:",gastos_anuales,"euros")
print(nombre.title(), "tiene unos ahorros anuales de:",ahorros_anuales,"euros")