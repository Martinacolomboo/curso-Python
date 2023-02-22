lista = list(range(2,101))
for num in lista:
	div = 0
	cant = num
	while (cant > 0):
        if (num % cant) == 0:
    	    div+=1
	    cant-=1
    if div==2:
  	    print(num)
'''-----------------------
for num in (range(2,101):
	primo=true
  for i in range(2,num)
  	if num % i==0:
    	primo= false
    if primo:
    	print(num)
-----------------------------------
for num in (range(2,101):
	primo=true
  i=2
  while primo==true and i<num:
  	if num % i==0
    	primo=false
    i+=1
  if primo:
  	print(num)'''
