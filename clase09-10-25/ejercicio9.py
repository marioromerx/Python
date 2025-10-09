cantidad=float(input("Introduce una cantidad a invertir: "))
interes=float(input("Introduce el interés anual: "))
anos=int(input("Introduce el número de años: "))

print ("El capital obtenido es: " + str(cantidad*(interes/100)*anos))