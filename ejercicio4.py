
numero1 = int(input("introduce el 1º:"))
numero2 = int(input("introduce el 2º:"))
numero3 = int(input("introduce el 3º:"))
numero4 = int(input("introduce el 4º:"))

lista = [numero1, numero2, numero3, numero4]
media = sum(lista) / len(lista)

print(f"la media de {numero1}, {numero2}, {numero3}, {numero4} es {media}")
