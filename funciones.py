from ast import While
from itertools import count
from lib2to3.pytree import WildcardPattern
from pickle import TRUE
import re
from tkinter import N


def sumadiguito(numero):
    suma=0
    while numero !=0:
        diguito=numero%10
        suma=suma+diguito
        numero = numero //10
        return suma
def primo (num):
    for i in range(2,num):
        if num % i==0:
            return False
    return TRUE

def frecuencia (numero,diguito):
    cantidad=0
    while numero !=0:
        ultdiguito= numero %10
        if ultdiguito == diguito:
            cantidad += 1
        numero = numero //10
    return cantidad
def factorial (numero):
    f=1
    if numero !=0:
        for i in range (1,numero +1):
            f=f*i
    return f

def maximo (a,b):
    if a>b:
        return a
    else:
        return b
def minimo(a,b):
    if a<b :
        return a
    else:
        return b 
def DNIvalidado(dni):
    cantidad=0
    while dni !=0:
        cantidad = cantidad +1
        dni=dni//10
    return cantidad ==7 or cantidad ==8
def lenUltimaPalabra(cadena):
    longuitud = len (cadena)
    if longuitud==0:
        return 0
    cantidad=0
    for i in range(longuitud):
        if cadena [i] !="":
            cantidad+=1
        else:
            if cadena [i]==i < (longuitud-1) and cadena [i+1] !=0:
                cantidad=0
    return cantidad

def obtenerIdentificador(nombre,dni):
    nombre= nombre.strip()
    i = nombre [0:nombre.find(" ")]
    i=i+str (lenUltimaPalabra(nombre))
    i=i+str (primerotresdiguitos(dni))
    return i
def primerotresdiguitos(numeros):
    while numeros>=1000:
        numeros =numeros/10
    return int (numeros)

def sumatoria(lista):
    suma=0
    for n in lista:
        suma+=n
    return suma
def numerosmenores(lista,limite):
    nueva=[]
    for n in lista:
        if n < limite:
            nueva.append  (n)
    return nueva
def frecuencia (lista):
    nueva=[]
    for n in lista:
        if (n,lista.count(n) )not in nueva : nueva.append((n, lista.count(n) ))
    return nueva   
        
def agregarpasajeros(pasajeros):
    nombre=input("nombre -x para cortar")
    while nombre != "x":
        dni=int(input("dni "))
        destino=int(input("ciudades de destino "))
        pasajeros.append ((nombre, dni , destino))
        nombre=int("nombre -x para cortar ")
    return pasajeros

def agregarciudades(ciudades):
    ciudad=input("ciudad-x para cortar")
    while ciudad != "x":
        pais=input("pais ")
        ciudades.append ((ciudades, pais))
        ciudad=input("ciudades -x para cortar ")
    return ciudades

def buscarciudades(pasajeros,dni):
    for viaje in pasajeros:
        if viaje [1] ==dni:
            return viaje [2]
    return ""

def cantidadpasajerociudad(pasajeros,ciudad):
    cantidad=0
    for viaje in pasajeros:
        if viaje [2] == ciudad:
            cantidad +=1
    return cantidad

def destino (pasajeros,ciudades,dmi):
    ciudadbuscada= buscarciudades (pasajeros,dmi)
    for ciudad in ciudades:
        if ciudad [0] == ciudadbuscada:
            return ciudad[1]
    return ""

def cantidadpasajerospais(pasajeros,ciudades,pais):
    cantidad=0
    for viaje in pasajeros:
        if pais== destino (pasajeros ,ciudades, viaje[1] ):
            cantidad +=1
    return cantidad

def cargarnombre(alumnos):
    nombre=input("nombre")
    while nombre !="x":
        alumnos.add(nombre)
        nombre = input ("nombre ")
        return alumnos

def direcciones (ventas):
    domicilios=set ()
    for venta in ventas:
        domicilios.add(ventas[3])
        return domicilios

def cargarsocio(socio):
    numero=int(input("numero de socios: "))
    while numero !=0:
        nombre=input("nombre y apellido: ")
        fecha=input("fecha de ingreso: ")
        cuota=input("cuota al dia : s/n")
        pago= cuota.lower()=="s"
        socio[numero]=[nombre,fecha,pago]
        numero=input("numero de socios: ")
    return socio

def modificar(socio,fechaanterior,fechanueva):
    for datos in socio.values():
        if datos [1]==fechaanterior:
            datos[1] = fechanueva
    return socio

def numeroso(socio,nombre):
    for numero,datos in socio.itens():
        if datos [0].lower()==nombre.lower:
            return numero
    return 0
def formatofecha(fecha):
    return fecha[:2]+"/"+fecha[2:4]
def imprimir(socio):
    for numero,datos in socio.items():
        print("numero",numero)
        print("nombre",datos)
        print("fecha de ingreso",formatofecha(datos[1]))
        if datos (2):
            print("cuota al dia")
        else:
            print("en deuda")
        print("----------")
    return None

