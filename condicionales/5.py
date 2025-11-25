tipo_id = input("Tipo de identificación (CC, PS, CE, CI): ")
nombres = input("Nombres: ")
apellidos = input("Apellidos: ")
genero = input("Género (M/F): ").upper()
anio = int(input("Año de nacimiento: "))
direccion = input("Dirección: ")
telefono = input("Teléfono: ")
salario = float(input("Salario actual: "))

salario_final = salario

if salario <= 1200000:
    if genero == "F":
        salario_final = salario * 1.10
    else:
        salario_final = salario * 1.08

elif salario > 1200000 and salario < 2000000:
    salario_final = salario * 1.05

else:  # salario >= 2000000
    if genero == "F":
        salario_final = salario * 1.03
    else:
        salario_final = salario * 1.025

print("\n--- RESULTADO FINAL ---")
print("Nombre:", nombres, apellidos)
print("Salario final:", salario_final)
