palabra = input("Introduce una palabra para comprobar si es palindromo: ").lower()
lista = list(palabra)
listainversa = list(lista)
listainversa.reverse()

if lista == listainversa:
    print (palabra, "es palindromo")
else:
    print (palabra, " no es palindromo")
