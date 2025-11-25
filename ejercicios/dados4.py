import random

# Pedir cuántas veces intentar antes de que se detenga automáticamente (seguridad)
N = int(input("¿Cuántas veces desea lanzar los dados como máximo? "))

intentos = 0

while intentos < N:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    print(f"Lanzamiento {intentos + 1}: {dado1} - {dado2}")

    # Verificar par de seis
    if dado1 == 6 and dado2 == 6:
        print("\n¡Salió PAR DE SEIS! El programa termina.")
        break

    intentos += 1

if intentos == N:
    print("\nSe alcanzó el número máximo de lanzamientos sin obtener par de seis.")
