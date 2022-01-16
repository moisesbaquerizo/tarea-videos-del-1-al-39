from funciones import *


nombre= input("nombre del socio: ")
while nombre !="":
    dni=int(input("dni del socio: "))
    while not (DNIvalidado)(dni):
        print("numeros invalidos ")
        dni= int (input("DNI des socio "))
    identificador=obtenerIdentificador (nombre,dni)
    print("el identificador del socio es. ",identificador)
    nombre= input("nombre del socio: ")
    
   
