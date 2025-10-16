puntuacion = int(input("Introduce la puntuacion del usuario: "))
if puntuacion == 0.0:
    print ("Nivel de rendimiento: Inaceptable, el usuario cobrará 2400€" )
elif puntuacion == 0.4:
    print ("Nivel de rendimiento: Aceptable, el usuario cobrará ", str(2400*1.4), "€")
elif puntuacion == 0.6:
    print ("Nivel de rendimiento: Aceptable, el usuario cobrará ", str(2400*1.6), "€")
else:
    print ("Valor no válido")