import random

aleatorio = random.randint(1,10)

adivinar = int(input("adiva el número del 1 al 10 ->"))

while adivinar != aleatorio:
    if adivinar > aleatorio:
        print("mu' alto pisha")
    else:
        print("mu' bajo cojone")
    adivinar = int(input("adiva el número del 1 al 10 ->"))
print("mu' bien Paconi")