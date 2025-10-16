edad = int(input("Introduce tu edad: "))
ingresos = int(input("Introduce tus ingresos mensuales: "))

if edad < 16:
    print("Debe ser mayor de 16")
else:
    if ingresos >= 1000:
        print("El usuario tributa")
    else:
        print("El usuario no tributa")