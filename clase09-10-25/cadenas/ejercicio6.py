frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

frase_modificada = frase.replace(vocal.lower(), vocal.upper())

print("Frase con la vocal en mayúscula: ", frase_modificada)
