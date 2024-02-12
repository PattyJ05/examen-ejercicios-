import random

numero = random.randint(1, 200)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 1 y el 200: "))
    intentos += 1

    if intento == numero:
        print("¡Correcto! Has logrado adivinar en", intentos, "intentos.")
        break
    elif intento < numero:
        print("El número es mayor. Intente de nuevo .")
    else:
        print("El número es menor. Intente de nuevo.")