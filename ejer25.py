cantidad=0
n= int(input("numero: "))
while n !=0 :
    primo=True
    for i in range(2,n ):
        if n%i==0:
            primo=False
    if primo :
        cantidad+=1
    n= int(input("numero: "))
print("primos: ",cantidad)
    
