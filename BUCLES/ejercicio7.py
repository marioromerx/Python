#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
x=1
y=1
for y in range (1,11):
    for x in range (1,11):
        print(x," x ",y, "=", x*y)
