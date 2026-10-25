def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    else:
        print("Todo bien:", resultado)
    finally:
        print("Esto siempre se ejecuta")

dividir(10, 2)
print("---")
dividir(10, 0)
