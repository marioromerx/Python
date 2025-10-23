pizza = input ("¿Quieres una pizza vegetariana?: ")
respuesta = pizza.lower()
if respuesta == "si":
    print ("INGREDIENTES PIZZA VEGETARIANA")
    print ("Pimiento, Tofu")

    ing = input("Elija 1 de los ingredientes: ")

    if ing.lower() == "pimiento":
        print ("La pizza lleva Tomate, Mozzarella y ", ing)
    elif ing.lower() == "tofu":
        print ("La pizza lleva Tomate, Mozzarella y ", ing)
    else:
        print ("Respuesta no válida")

elif respuesta == "no":
    print ("INGREDIENTES PIZZA NO VEGETARIANA")
    print ("Peperoni, Jamón, Salmón")

    ing = input("Elija 1 de los ingredientes: ")
    ing = ing.lower()

    if ing.lower() == "peperoni":
        print ("La pizza lleva Tomate, Mozzarella y ", ing)
    elif ing.lower() == "jamon":
        print ("La pizza lleva Tomate, Mozzarella y ", ing)
    elif ing.lower() == "salmon":
        print ("La pizza lleva Tomate, Mozzarella y ", ing)
    else:
        print ("Respuesta no válida")
else:
    print ("Respuesta erronea, debe responder si o no")