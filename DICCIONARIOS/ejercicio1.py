divisas = {"Euro": "€", "Dollar":"$", "Yen":"¥"}
moneda = input ("Introduce la divisa para mostrar su simbolo: ")

if moneda.title() in divisas:
    print(divisas[moneda.title()])
else:
    print("La divisa no está en el diccionario")