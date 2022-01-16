letra=input("letra:")
if len(letra)  != 1 :
    print("dever ser solo letra")
else:
    if letra in "aeiou:":
        print(" es vocal")
    else:
        print("no es vocal")    
        
