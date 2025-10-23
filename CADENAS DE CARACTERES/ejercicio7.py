correo = input("Introduce tu correo electrónico: ")
nombre = correo.split('@')[0]
nuevo_correo = nombre + "@ceu.es"
print("Tu nuevo correo es:", nuevo_correo)
