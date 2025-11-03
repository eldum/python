#1
lista = [3,5,7,21]
def mayor():
    lista.sort
    print(lista[-1])
mayor()

#2
palabra = "palabra"
n = 0
def contar():
    print(len(palabra))
contar()

#3
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
if es_primo(7):
    print("es primo")
else:
    print("no es primo")
#4
def repetir():
    lista = [1, 2, 2, 3, 4, 4, 5]
    sin_repetidos = list(set(lista))
    print(sin_repetidos)
repetir()
#5
def calculadora():
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    ignorar = int(input("Elige opción del MENÚ:"))
    while True:
        print(eval(input("Introduce una operación:")))
        print("\n--- MENÚ ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. salir")
        ignorar = int(input("Elige opción del MENÚ:"))
        if ignorar == 5:
            print("Adios")
            break
calculadora()

