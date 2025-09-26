#Escribir un programa que pregunte al usuario una cantidad a invertir
#el interes anual y el numero de años, y muestre por pantalla el capital
#obtenido en la inversión


cantidad=float(input("Introduce la cantidad a invertir: "))
interes_anual=float(input("Introduce el interés anual: "))
anos=float(input("Introduce el número de años: "))

capital=cantidad*(1 + interes_anual / 100) ** anos

print("El capital obtenido después de ",anos, "es: ", capital)