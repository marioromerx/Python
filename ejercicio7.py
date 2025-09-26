#Escribir un programa que pida al usuario su peso (en kg) y 
# estatura (en metros), calcule el índice de masa corporal y lo almacene
# en una variable, y muestre por pantalla la frase "Tu indice de masa corporal es <imc>"
#Donde <imc> es el indice de masa corporal calculado redondeado con dos decimales.
peso=float(input("Introduce tu peso: "))
estatura=float(input("Introduce tu estatura: "))
imc= peso/ (estatura ** 2)
print(imc)
print("Tu índice de masa corporal es ", round(imc,2))