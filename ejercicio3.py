def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except TypeError:
        print("Solo se pueden dividir numeros")
    else:
        print("Todo bien:", resultado)
    finally:
        print("Esto siempre se ejecuta")

dividir(10, 2)
print("---")
dividir(10, 0)
print("---")
dividir("a", 2)
