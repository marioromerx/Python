#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
#a mayor.
numeros = []

for i in range(0,6):
    n = int(input("Introduce el número ganador "))
    numeros.append(n)
    
numeros.sort()
print("Los numeros ordenados son", numeros)
