nombre=str(input("Introduce tu nombre: "))
sexo=str(input("Introduce tu sexo M mujer o H hombre: "))

nombre=nombre.lower()
inicial = nombre[0]
if (inicial <= "m" and sexo == "M") or (inicial >= "n" and sexo == "H"):
    print ("Es del grupo A")
else:
    print ("Es del grupo B")