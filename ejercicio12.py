numeros = str(input("pon números separados por espacios: "))

partes = numeros.split( )

intnumeros = list(map(int, partes))

print(sum(intnumeros))