linea = int(input("Cuantas lineas?: "))
barato = []
medio = []
caro = []
lista_cantidad = []
total_bruto = 0

for i in range(linea):
    while True:
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            if precio >= 0 and cantidad >= 1:
                break
            else:
                print("El precio debe ser mayor o igual a 0 y la cantidad mayor o igual a 1.")
        except ValueError:
            print("Introduce valores válidos.")
    
    total_bruto += precio * cantidad
    lista_cantidad.append(cantidad)
    
    if precio < 5:
        barato.append(precio)
    elif precio < 20:
        medio.append(precio)
    else:
        caro.append(precio)

print(f"Cantidad: {lista_cantidad}")
print(f"Barato: {barato}, Medio: {medio}, Caro: {caro}")
print(f"Total bruto: {total_bruto:.2f}")

if total_bruto < 20:
    descuento = total_bruto
    code = "0%"
elif total_bruto < 50:
    descuento = total_bruto * 0.95
    code = "5%"
elif total_bruto < 100:
    descuento = total_bruto * 0.90
    code = "10%"
else:
    descuento = total_bruto * 0.85
    code = "15%"

iva = descuento * 1.10  

print(f"Descuento aplicado: {code}")
print(f"Total con descuento: {descuento:.2f}")
print(f"Total con IVA (10%): {iva:.2f}")

mac = max(lista_cantidad)
mic = min(lista_cantidad)
print(f"Mínimo: {mic} y Máximo: {mac}")