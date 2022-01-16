corrimiento= int(input("corimiento: "))
alfabeto="abcdefghijklmnñopqrstvuwxyz"

for i in range(5):
    men=input("mensaje incriptado: ")
    encriptado = ""
    for caracter in men:
        if caracter.lower() in alfabeto:
            ind= alfabeto.find(caracter.lower())
            ind= (ind + corrimiento)%27
            encriptado+=alfabeto[ind]
        else:
            encriptado+= caracter
    print("mensaje encriptado:  ", encriptado)

      
