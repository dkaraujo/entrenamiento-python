def f(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

f(1)
f(1, 2, 3, 4, x=5)
f(10, 20, 30, nombre="Diana", ciudad="Murcia")
f(7, 8, 9, 10, 11, color="rojo", talla=42)
