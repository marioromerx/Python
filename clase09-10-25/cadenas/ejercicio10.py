cesta = input("Introduce los productos de la cesta de la compra, separados por comas: ")
productos = cesta.split(',')
for producto in productos:
    print(producto.strip()) 