#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo POR ACABAR
n = int(input("Introduce un número: "))
for x in range (1,n+1):
    if x % 2 == 1:
        espacio= ""
    for i in range(x,0, -2):
            espacio += str(i)+ ""
            print(espacio)

