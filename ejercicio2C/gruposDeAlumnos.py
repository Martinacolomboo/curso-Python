genero = input("Ingrese el genero: ")
genero = genero.lower()
nombre = input("Ingrese el nombre: ")
nombre = nombre.title()
if genero == "chica":
    if "E" <= nombre[0] <= "M":
        print("Le corresponde el grupo A")
    else:
        print("Le corresponde el grupo B")
else:
    if ("A" <= nombre[0] <= "H") or ("R" <= nombre[0] <= "Z"):
        print("Le corresponde el grupo A")
    else:
        print("Le corresponde el grupo B")
    