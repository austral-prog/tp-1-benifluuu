def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    Horas_completas = total_segundos // 3600
    Minutos_completos_restantes = 65 // 60
    Segundos_completos_restantes = 65 % 60

    print(Horas_completas)
    print(Minutos_completos_restantes)       
    print(Segundos_completos_restantes)

#time()
