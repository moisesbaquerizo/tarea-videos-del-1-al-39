denlinea=0
clineas=0
titulo=input("titulo del libro: ")
while titulo != "":
    if titulo=="/":
        clineas+=1
        print("lineas completada. Aparecen", denlinea,"diguitos")
        denlinea=0
    else:
        for caracter in titulo:
            if caracter in titulo:
                if caracter in "0123456789":
                    denlinea+=1
    titulo=input("titulo del libro: ")
print("fin se leyeron",clineas,"lineas")


