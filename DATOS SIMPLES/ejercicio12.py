barras = float(input("¿Cuántas barras no son del dia?: "))
precio = 3.49
descuento = (precio*barras*0.6)
total=(precio*barras)-descuento

print ("El precio habiutal de la barra es de "+str(precio)+"€")
print ("El descuento que se le hace es de "+str(descuento)+"€")
print("coste final total: "+str(round(total, 2))+"€")