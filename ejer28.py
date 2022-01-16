def sumadiguito(numero):
    suma=0
    while numero !=0:
        diguito=numero%10
        suma=suma+diguito
        numero = numero //10
        return suma
    
num= int(input( "numero a procesar: "))
while num !=0:
    print(" suma: ",sumadiguito(num))
    num= int(input("numero a procesar "))
     
        
        
