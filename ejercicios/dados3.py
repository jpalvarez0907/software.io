import random

# Pedir cuántas veces lanzar el dado
veces = int(input("¿Cuántas veces deseas lanzar el dado? "))

# Contadores para cada número
c1 = c2 = c3 = c4 = c5 = c6 = 0

# Lanzamientos
for i in range(veces):
    num = random.randint(1, 6)

    if num == 1:
        c1 += 1
    elif num == 2:
        c2 += 1
    elif num == 3:
        c3 += 1
    elif num == 4:
        c4 += 1
    elif num == 5:
        c5 += 1
    else:
        c6 += 1

# Mostrar resultados
print("\nResultados:")
print("Número 1 salió:", c1, "veces")
print("Número 2 salió:", c2, "veces")
print("Número 3 salió:", c3, "veces")
print("Número 4 salió:", c4, "veces")
print("Número 5 salió:", c5, "veces")
print("Número 6 salió:", c6, "veces")
