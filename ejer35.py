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
