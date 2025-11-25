import random

total_tiros = 0
suma_total = 0
pares = 0
impares = 0

continuar = "s"

while continuar.lower() == "s":
    # Lanzar el dado
    num = random.randint(1, 6)
    print(f"Salió: {num}")

    # Actualizar contadores
    total_tiros += 1
    suma_total += num

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Preguntar si desea continuar
    continuar = input("¿Deseas lanzar de nuevo? (s/n): ")

# Reporte final
print("\n--- REPORTE FINAL ---")
print("Total de tiros efectuados:", total_tiros)
print("Suma total de los tiros:", suma_total)
print("Total de pares generados:", pares)
print("Total de impares generados:", impares)
