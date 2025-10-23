cantidad = float(input("Cantidad depositada en la cuenta de ahorros: "))

print("El primer año:", round(cantidad * 1.04, 2))
print("El segundo año:", round(cantidad * 1.04**2, 2))
print("El tercer año:", round(cantidad * 1.04**3, 2))