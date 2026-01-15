curso = {
    "Matematicas":6,
    "Fisica":4,
    "Quimica":5
}
totalcreditos = 0
for asignatura, creditos in curso.items():
        print("La ", asignatura, "tiene", creditos, "créditos")
        totalcreditos = totalcreditos+creditos
print("El numero total de creditos que tiene el curso es: ", totalcreditos)