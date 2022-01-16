ainicio=int(input("año inicial: "))
afin=int(input("año final: "))
for año in range(ainicio,afin):
    if not año % 10==0:
        continue
    if not año % 4==0:
        continue
    if año % 100!=0 or año % 400 ==0:
        print(año)
