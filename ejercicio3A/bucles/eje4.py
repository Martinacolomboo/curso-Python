frase = input("Ingrese una frase: ")
letra=input("Ingrese una letra: ")
cont=0
for i in range(len(frase)):
	if (frase[i]==letra):
  	    cont+=1
print(cont)