print("Ingrese dos números:")
a = float(input("Número 1: "))
b = float(input("Número 2: "))

print("""
[1] Sumar
[2] Restar
[3] Multiplicar
[4] Dividir
[5] Todas
""")

op = int(input("Elija una opción: "))

if op == 1:
    print("Suma:", a + b)
elif op == 2:
    print("Resta:", a - b)
elif op == 3:
    print("Multiplicación:", a * b)
elif op == 4:
    if b != 0:
        print("División:", a / b)
    else:
        print("No se puede dividir entre cero")
elif op == 5:
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicación:", a * b)
    if b != 0:
        print("División:", a / b)
    else:
        print("División: No definida (b = 0)")
else:
    print("Opción inválida")
