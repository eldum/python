nota = float(input("Introduce una nota (0–10): "))

if 0 <= nota <= 10:
    if nota < 5:
        categoria = "Insuficiente"
    elif nota < 6:
        categoria = "Suficiente"
    elif nota < 7:
        categoria = "Bien"
    elif nota < 8:
        categoria = "Notable"
    elif nota < 9:
        categoria = "Sobresaliente"
    else:  
        categoria = "Sobresaliente"
else:
    categoria = "Nota no válida"

print(categoria)