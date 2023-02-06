lista1=list(range(1,15))
max=0
max2=0
for i in lista1:
    if max<=i:
        max2=max
        max=i
print("el segundo numero mas grande es", max2)     