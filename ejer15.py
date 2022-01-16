fecha=input(" fecha (formato dia dd/mm): ")
fecha = fecha.lower()
diaseman=fecha[0:fecha.find(",")]
nro= int(fecha [ fecha.find(" ")+1:fecha.find("/") ])
mes= int(fecha [ fecha.find("/")+1: ])
if nro >31 or mes >12:
    print("fecha correcta")
else:
    if diaseman in "lunes,martes,miercoles":
        res=input("ingrese s / n")
        if res.lower()=="s":
            apr=int(input("cantidad de aprovados"))
            repr=int(input("cantidad de reprobados"))
            print("porcentaje de aprobados ",(apr*100)/(apr+repr),"%")
    elif diaseman == "jueves":
        asis=int(input("cantidad de asistencia"))
        if asis > 50:
            print("asistio la mayoria")
        else:
            print(" no asistio la mayoria")
    elif diaseman == "viernes":
        if nro ==1 and (mes ==1 or mes ==7):
            print("comienzo de un nuevo siclo:")
            alu=int(input("cantidad de alumnos: "))
            ara=float(input("aranse: "))
    else:
        print("fecha incorrecta")
            
print("fin del programa")
    
