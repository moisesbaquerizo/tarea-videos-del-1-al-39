#dia=int(input("dia de su nacimiento: "))
#mes=int(input("mes de su nacimiento: "))
#año=int(input("año de su nacimiento: "))
#print(dia,"/",mes,"/",año,"/")

#----solicitan de otra forma -----
fecha=int(input("fecha en formato ddmmaa: "))
año= fecha/10000
#año= fecha [ :2]
dia= fecha/1000000
#dia= fecha[2:4]
mes= (fecha/10000)%100
#año= fecha [4:]
print(dia,"/",mes,"/",año,"/")
