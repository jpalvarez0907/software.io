import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("Dado 1:", dado1)
print("Dado 2:", dado2)

# Validar par o impar
print("Dado 1 es:", "PAR" if dado1 % 2 == 0 else "IMPAR")
print("Dado 2 es:", "PAR" if dado2 % 2 == 0 else "IMPAR")

# Validar iguales
if dado1 == dado2:
    print("YOU WIN")
else:
    print("GAME OVER")
