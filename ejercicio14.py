nombres = input("Introduce números separados por comas: ").split(",")
nombres = [n.strip() for n in nombres]
print(", ".join(nombres[::-1]))