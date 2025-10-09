nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))

coste_total = precio * unidades
precio_redondeado = round(precio, 2)
coste_total_redondeado = round(coste_total, 2)
print("El producto "+str(nombre)+" con precio unitario de "+str(precio_redondeado)+" y " +str(unidades)+" unidades tiene un coste total de "+str(coste_total_redondeado)) 