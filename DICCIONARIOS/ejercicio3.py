frutas = {
    "Platano" : 1.35,
    "Manzana" : 0.80,
    "Pera" : 0.85,
    "Naranja" : 0.70
}

fruta = input("Introduce una fruta: ")
kg = float(input ("Di el nº de kilos: "))

if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else:
    print("La fruta "+fruta+" no está en la lista")