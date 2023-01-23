burger = input("Quiere una hamburguesa clasica o vegana? ").lower()
if burger == "vegana":
    print("Los ingredientes extra son: tofu y cebolla caramelizada")
    tofu = bool(input("Quiere tofu? Si no quiere, aprete Enter: "))
    cebolla = bool(input("Quiere cebolla? Si no quiere, aprete Enter: "))
    print("Se eligió la hamburguesa",burger,"-tofu:",tofu,"-cebolla:",cebolla)
else:
    print("Los ingredientes extra son: queso, bacon y huevo")
    queso = bool(input("Quiere queso? Si no quiere, aprete Enter: "))
    bacon = bool(input("Quiere bacon? Si no quiere, aprete Enter: "))
    huevo = bool(input("Quiere huevo? Si no quiere, aprete Enter: "))
    print("Se eligió la hamburguesa",burger,"-queso:",queso,"-bacon:",bacon,"-huevo:",huevo)
