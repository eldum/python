lista = []
posiciones = []
while True:
    try:
        añadir = int(input("añade número: "))
        if 0 == añadir:
            print("se acabo")
            break
        else:
            lista.append(añadir)
    except ValueError:
        print("pon un número")
numero = int(input("Ingrese un número: "))

for i in range(len(lista)):
    if lista[i] == numero:
        posiciones.append(i)

print(f"El número {numero} aparece en las posición: {posiciones}")

