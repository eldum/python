factura = []

while 0 not in factura:
    try:
        precio = float(input("mete precio -> "))
        factura.append(round(precio,2))
    except:
        break

factura.pop()

print(f"esta es su factura {factura}")