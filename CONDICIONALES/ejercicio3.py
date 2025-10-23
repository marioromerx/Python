n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

div = int(n1/n2)
if n2 == 0:
    print("El divisor no puede ser 0 ")
else:
    print ("Resultado: " + str(div))