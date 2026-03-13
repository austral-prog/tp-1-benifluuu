def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    Monto_impuesto = 100 * 0.21
    Subtotal = precio_base + Monto_impuesto
    Monto_propina = Subtotal * 0.10
    Precio_final = Subtotal + Monto_propina
    
    print(Monto_impuesto)
    print(Subtotal)
    print(Monto_propina)
    print(Precio_final)

#price()






