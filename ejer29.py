def sumadiguito(numero):
    suma=0
    while numero !=0:
        diguito=numero%10
        suma=suma+diguito
        numero = numero //10
        return suma
sumatoria=0
num=int(input("numero a procesar: "))
while num !=0:
    print("suma: ",sumadiguito(num))
    sumatoria+=num
    num=int(input("numero a procesar: "))
print("sumatoria: ",sumatoria)
print("diguito: ",sumadiguito(sumatoria))
    
    
