def validar (email):
    caraterBuscador= "@"
    emailvalido= False
    for c in email:
        if c == caraterBuscador:
            emailvalido=True
            break
    return emailvalido
direccion=input("tu email. ")
if validar(direccion):
    print("direccion validar")
else:
    print("direccion invalida")
    
         
