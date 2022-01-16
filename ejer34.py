def DNIvalidado(dni):
    cantidad=0
    while dni !=0:
        cantidad = cantidad +1
        dni=dni//10
    return cantidad ==7 or cantidad ==8
print (DNIvalidado(340))
print (DNIvalidado(4556.7687))
