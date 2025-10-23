contrasena = ("contraseña")
respuesta = str(input("Introduce la contraseña: "))
if respuesta.lower() == contrasena.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")