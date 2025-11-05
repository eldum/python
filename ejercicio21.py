import time 
import random

adivinar = random.randint(1, 10)
inicio = time.time()

while True:
    if time.time() - inicio > 10:
        print("Se acabó el tiempo")
        break
    try:
        prueba = int(input("Número: "))
        if prueba == adivinar:
            print("Buena ")
            break
        elif prueba > adivinar:
            print("Alto")
        else:
            print("Bajo")
    except ValueError:
        print("mete un número correcto")

print(f"El número era: {adivinar}")