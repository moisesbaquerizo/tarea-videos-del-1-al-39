contadores= []
alfaveto="abcdefghijklmnñopqrstuvwxyz"
for letra in alfaveto+alfaveto.upper():
    contadores [letra] =0
for i in  range (3):
    cadena =input("cadena de caracteres: ")
    for caracter in cadena:
        if caracter.lower( ) in alfaveto:
            contadores[caracter ]+=1
for caracter, cantidad in contadores.items():
    print(caracter,":",cantidad)
    
