precio = float(input("Introduce el precio del producto: "))
euros = int(precio)
centimos = int(round((precio - euros) * 100))
print ("El precio en euros es de: "+str(euros)+"€ y "+str(centimos)+" centimos")