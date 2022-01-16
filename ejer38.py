
from funciones import *
pasajeros=[]
ciudades=[]
while True :
    print("1 agregar pasajeros ")
    print("2 agregar ciudades ")
    print("3 buscar ciudades de destino mediante el dni")
    print("4 cantidad de pasajeros que viajan a una ciudad")
    print("5 buscar pais de destino mediante dni")
    print("6 cantidad de pasajeros que viajan a un pais ")
    print("7 salir del programa")
    op=int(input("accion a ejecutar"))
    if op==1:
        print("agregar pasajeros")
        pasajeros=agregarpasajeros(pasajeros)
        
    if op==2:
        print("agregar ciudades")
        ciudades=agregarciudades(ciudades)
        
    elif op==3:
        dni=int(input("dni: "))
        print("el pasajero viaja a: ",buscarciudades(pasajeros,dni))
        
        
    elif op==4:
        ciudad=input("ciudad: ")
        print("viajan: ",cantidadpasajerociudad(pasajeros,ciudad),"pasajeros")
        
    elif op==5:
        dni=int(input("dni: "))
        print("viaja a: ",destino(pasajeros,ciudades,dni))
        
    elif op==6:
        pais=input("pais: ")
        print(" viaja a: ",cantidadpasajerospais(pasajeros,ciudades,pais),"pasajeros")
        
    elif op==7:
        break
