def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9

    Promedio= (nota1 + nota2 + nota3)/3
    Nota_maxima = nota3
    Nota_minima = nota2
    Puntos_faltanes = 10 - Promedio

    print(Promedio)
    print(Nota_maxima)
    print(Nota_minima)
    print(Puntos_faltanes)

#grades()

