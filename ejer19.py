snegativo=0
spositivos=0
canpo=0
for i in range(6):
    num=int(input("numero: "))
    if num >=0:
        canpo +=1
        spositivos+=num
    else:
        snegativo+=num
print("suma de negativos", snegativo)
if canpo != 0:
    print("promedio de positivos: ", spositivos/canpo)
else:
    print("no se ingresaron los positivos")
     
