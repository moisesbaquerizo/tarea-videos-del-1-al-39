
from funciones import *


numero=[]
nro=int(input("numero: "))
while nro!=0:
    numero.append(nro)
    nro=int(input("numero: "))
    
eliminar=int(input("numero a eliminar : "))
if eliminar in numero:
    numero.remove(eliminar)
else:
    print("ese numero no esta entre los ingresados ")
print("sumatoria de los numeros " ,sumatoria(numero))

limite=int(input("filtrar numeros menores a: "))
for n in numerosmenores(numero,limite):
    print(n)
print("frecuencia ")
for tupla in frecuencia(numero):
    print (tupla (0),"aparese",tupla(1),"veses" ) 
    
    
