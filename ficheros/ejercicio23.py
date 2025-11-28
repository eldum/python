def leer_personas(fichero):
    personas = []
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:  
                    partes = linea.split(";")  
                    if len(partes) == 2:
                        nombre = partes[0].strip()
                        try:
                            edad = int(partes[1].strip())
                            personas.append((nombre, edad))
                        except ValueError:
                            pass
    except FileNotFoundError:
        print("El fichero no existe.")
    return personas


def obtener_edad(persona):
    return persona[1]


def persona_mas_joven(personas):
    return min(personas, key=obtener_edad)


def persona_mas_vieja(personas):
    return max(personas, key=obtener_edad)

# Programa principal
personas = leer_personas("personas.txt")

if personas:
    joven = persona_mas_joven(personas)
    vieja = persona_mas_vieja(personas)
    print(f"Más joven: {joven[0]} ({joven[1]} años)")
    print(f"Más vieja: {vieja[0]} ({vieja[1]} años)")
else:
    print("No hay datos validos")