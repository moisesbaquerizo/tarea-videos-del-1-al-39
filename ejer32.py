from subprocess import REALTIME_PRIORITY_CLASS


def maximo (a,b):
    if a>b:
        return a
    else:
        return b
def minimo(a,b):
    if a<b :
        return a
    else:
        return b 
x=int(input("un numero: "))
y=int(input("otro numero: "))
print(maximo(x-3,minimo(x+2, y-5))) 
    
    
