tpares=0
timpares=0
num=int(input("numero: "))
while num != 0:
    pares=0
    inpares=0
    while num != 0:
        uldigito=num%10
        if uldigito %2==0:
            pares+=1
            tpares+=1
        else:
            inpares+=1
            timpares+=1
        num=num//10
    print("el numero ingresado tiene",pares,"diguitos paresy ",inpares,"diguitos impares")
    num=int(input("numero: "))
print("total de diguitos pares: ",tpares)

print("total de diguitos impares: ",timpares)
