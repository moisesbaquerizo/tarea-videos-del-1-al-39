
from funciones import *
primaria=set()
secundaria=set()
print("alumnos de primaria")
primaria=cargarnombre(primaria)
print("alumno de secundaria")
secundaria=cargarnombre(secundaria)
print("nombre de todos los alumnos")
for nombre in primaria |secundaria:
    print(nombre)
print("nombre comunes")
for nombre in primaria&secundaria:
    print(nombre)
print("nombre de primaria que no se repiten en secundaria ")
for nombre in primaria-secundaria:
    print(nombre)
        
