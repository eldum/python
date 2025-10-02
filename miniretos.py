nums = [3, 7, 2, 9]

# 1. Suma de todos
suma = 0
for n in nums:
    suma += n
print(f"1) Suma de todos: {suma}")

# 2. Máximo
maximo = nums[0]
for n in nums:
    if n > maximo:
        maximo = n
print(f"2) Máximo: {maximo}")

# 3. Contar ocurrencias de un número
x = 7
contador = 0
for n in nums:
    if n == x:
        contador += 1
print(f"3) {x} aparece {contador} veces")

# 4. Media de la lista (sin sum)
total = 0
contador = 0
for n in nums:
    total += n
    contador += 1
media = total / contador if contador > 0 else 0
print(f"4) Media: {media}")

# 5. Lista con los pares
pares = []
for n in nums:
    if n % 2 == 0:
        pares.append(n)
print(f"5) Pares: {pares}")

# 6. max(nums) - min(nums)
maximo = nums[0]
minimo = nums[0]
for n in nums:
    if n > maximo:
        maximo = n
    if n < minimo:
        minimo = n
print(f"6) Diferencia max - min: {maximo - minimo}")

# 7. Buscar primer índice de un número
x = int(input("7) Número a buscar: "))
indice = -1
for i in range(len(nums)):
    if nums[i] == x:
        indice = i
        break
print(f"   Índice: {indice}")
