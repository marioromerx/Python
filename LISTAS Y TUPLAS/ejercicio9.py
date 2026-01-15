palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    a = 0
    for letra in palabra:
        if letra == vocal:
            a += 1
    print("La vocal"+vocal+" aparece "+str(a)+" veces") 