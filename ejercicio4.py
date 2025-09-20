lista = []

for i in range(4):
    lista.append(int(input("escribe el número:")))

media = sum(lista) / len(lista)

print(f"la media de {lista} es {media}")