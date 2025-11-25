import random

# Lanzar el dado (número entre 1 y 6)
numero = random.randint(1, 6)

print("Número generado:", numero)

# Verificar si es par o impar
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
