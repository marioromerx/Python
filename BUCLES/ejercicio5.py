cantidad = int(input("Ingrese la cantidad a invertir: "))
interes = int(input("Ingrese el interés anual: "))
anos = int(input("Ingrese la cantidad de años a invertir: "))

for x in range(0,anos+1):
    capital = cantidad * (1+ interes / 100) ** x
    print("Después de", x, "años, el capital es de:", capital)