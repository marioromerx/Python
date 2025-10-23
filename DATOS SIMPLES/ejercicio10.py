payasos = int(input("¿Cuántos payasos se han vendido en el ultimo pedido?: "))
muñecas = int(input("¿Cuántas muñecas se han vendido en el ultimo pedido?: "))
total = (payasos*112+muñecas*75)/1000
print("El peso total del paquete que será enviado es de "+str(total))