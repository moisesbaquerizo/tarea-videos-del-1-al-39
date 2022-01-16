cadena= "si, profesor, es cierto... yo me comi mi tarea"
print(cadena[10])
print(cadena[-1])
print(cadena[0:9])
print(cadena[ ::3 ])
print(cadena[ ::-1 ])
print(cadena[4:9])

#------------------
s= "     hola, ¿como estas?"
print(s[ ::-1])
#print( s [len(s)) produce un error 
print( s [len(s)-1 ])
print(s.count("0"))
print( s.count("hola"))
print( s[-4:])
print(s[15:] )
print(s.find("o"))
print(s.strip())
#print(x=s.upper())
#print(x==s)
print(s[14: ].upper())
print( len(s) )
print(s.replace(" ", "*"))
print(s.replace("z","Z"))
#--------------------
x="programar en python"
print(x[-1])
print(x[len(x)-1])

cadena="hola"
print(cadena.find("2"))
print("a" in "datiles")
print("me gusta programar".find(" "))
print("me gusta programar".count(" "))
#print(cadena [0]="H")
#print(nueva="c"+cadena[1: ])
w= "hoy es miercoles"
print(w.replace("i",("í")))
print(w.replace("i",("í").replace("e",("é"))))
print(w.count("a")+w.count("e")+w.count("i")+w.count("o")+w.count("u")  )
