nombreN = int(input("cuántos números vas a poner? ->"))
listaN = []


print(f"escribe {nombreN} números ->")

for i in range(nombreN):
    numeros = int(input(f"escribe el {i+1}º número -> "))
    listaN.append(numeros)

print(f"el mayor es {max(listaN)} y el menor es {min(listaN)}")

