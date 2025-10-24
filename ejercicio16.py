# Identidad.py

N = int(input("Tamaño de la matriz: "))
mat = []

for i in range(N):
    fila = list(map(int, input(f"Fila {i+1} (separa números con espacio): ").split()))
    mat.append(fila)

es_identidad = True
for i in range(N):
    for j in range(N):
        if (i == j and mat[i][j] != 1) or (i != j and mat[i][j] != 0):
            es_identidad = False

print("Es matriz identidad." if es_identidad else "No es matriz identidad.")
