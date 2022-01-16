total= 0
monto=float(input("monto de la venta: "))
while monto != 0:
    if monto<0:
        print("monto no valido")
    else:
        total+=monto
        monto=float(input("monto de la venta: "))
if total>1000:
    total-= total*0.1
print("monto total a pagar: ", total)
    
