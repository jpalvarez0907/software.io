import random
#pedir cuantas veces lanzar el dado 
veces= int(input("Cuantas veces deseas lanzar el dado?"))
suma_total=0
#Lanzar el dado de la cantidad 
for i in range (veces):
    numero = random .randint(1,6)
    print(f"lanzamienton {i+1} : {numero}")
    suma_total+=numero
    print("nSuma total de los valores generados :", suma_total)
    