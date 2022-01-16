CAPACIDADM2=4
XJEGRADAS=0.2
XESPECIALES=0.3
XCOMUNES=0.7
dimenciones=float(input("dimenciones en (m2): "))
gradas=int(input("cantidad de personas que caben en las gradas:"))
xesenario=int(input("porcentaje que ocupa las gradas :")) 
m2gradas= dimenciones*XJEGRADAS
m2esenario= dimenciones*(xesenario/100)
m2disponible=dimenciones - m2gradas - m2esenario
peronastotales= (m2disponible*4)*gradas 

print("caben",peronastotales,"personas")
presioent=float(input("presio entrada especiales: "))
presiocomun=float(input("presio entrada comun: "))
print("ingreso total de ventas: ",(peronastotales*presioent)*presioent + (peronastotales*presiocomun)*presiocomun)
