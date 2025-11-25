import random

# Pedir cuántas veces lanzar el dado
veces = int(input("¿Cuántos lanzamientos vas a efectuar? "))

pares = 0
impares = 0

for i in range(veces):
    num = random.randint(1, 6)
    print(f"Lanzamiento {i+1}: {num}")

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Resultados finales
print("\nRESULTADOS:")
print("Tiros pares: ", pares)
print("Tiros impares:", impares)
