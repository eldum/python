print("Ingresa los nombres:")
archivo = open("personas.txt", "w")

nombre = input("Nombre: ")
while nombre != "":
    archivo.write(nombre + "\n")
    nombre = input("Nombre: ")

archivo.close()

print("\nLeyendo los nombres...")
archivo = open("personas.txt", "r")
lineas = archivo.readlines()
archivo.close()

nombres = []
for linea in lineas:
    nombres.append(linea)

print("\nNombres ordenados:")
nombres.sort()
for n in nombres:
    print(n)
