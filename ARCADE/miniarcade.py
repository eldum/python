import random
from datetime import datetime
#La dificultad secreta es la 5 <================================================
#/\
#||
#||
#||
#||
#||

# Archivo de registros en el mismo directorio
def guardar_record(nivel, palabra, resultado, errores, intentos_max):
    """Guarda una línea en record.txt con fecha, nivel, palabra, resultado y errores."""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fecha} | {nivel} | {palabra.upper()} | {resultado} | Errores: {errores}/{intentos_max}\n"

    try:
        with open("record.txt", "a", encoding="utf-8") as f:
            f.write(linea)
    except:
        pass


def jugar_ahorcado():
    palabras_facil = [
        "sol", "mar", "ave", "rio", "luz", "paz", "rey", "ley",
        "pan", "sal", "dos", "mes", "oro", "luz", "gas", "fin"
    ]
    
    palabras_medio = [
        "juego", "plaza", "tiempo", "casa", "libro", "flores",
        "campo", "mesa", "silla", "puerta", "ventana", "camino"
    ]
    
    palabras_dificil = [
        "computadora", "algoritmo", "programacion", "tecnologia",
        "informacion", "desarrollo", "laberinto", "misterioso",
        "arquitectura", "extraordinario", "telecomunicaciones"
    ]
    
    palabras_euskera = [
        "kaixo", "eskerrik", "agur", "etxe", "itsaso", "mendi",
        "liburua", "ordenagailu", "janaria", "txakurra", "katu",
        "lagun", "familia", "eskola", "irakasle", "ikasle"
    ]
    
    palabras_valenciano = [
        "hola", "adeu", "gracia", "casa", "platja", "muntanya",
        "llibre", "ordinador", "menjar", "gos", "gat", "amic",
        "familia", "escola", "mestre", "alumne", "aigua", "foc"
    ]
    
    dibujo = [
        """
        
        
        
        =========""",
        """
        
        |
        |
        |
        =========""",
        """
        +---+
        |
        |
        |
        =========""",
        """
        +---+
        |   O
        |
        |
        =========""",
        """
        +---+
        |   O
        |   |
        |
        =========""",
        """
        +---+
        |   O
        |  /|\\
        |
        =========""",
        """
        +---+
        |   O
        |  /|\\
        |  / \\
        ========="""
    ]
    
    # Selección de dificultad
    print("\n=== SELECCIONA DIFICULTAD ===")
    print("1) Fácil (palabras cortas 3-4 letras)")
    print("2) Medio (palabras de 5-7 letras)")
    print("3) Difícil (palabras largas 8+ letras)")
    print("4) Euskera (palabras en euskera)")
    
    while True:
        opcion = input("\nElige dificultad (1/2/3/4): ").strip()
        if opcion == "1":
            palabras = palabras_facil
            nivel = "FÁCIL"
            break
        elif opcion == "2":
            palabras = palabras_medio
            nivel = "MEDIO"
            break
        elif opcion == "3":
            palabras = palabras_dificil
            nivel = "DIFÍCIL"
            break
        elif opcion == "4":
            palabras = palabras_euskera
            nivel = "EUSKERA"
            break
        elif opcion == "5":
            palabras = palabras_valenciano
            nivel = "VALENCIÀ"
            break
        else:
            print("Opción inválida. Elige 1, 2, 3, 4.")
    
    palabra = random.choice(palabras).lower()
    letras_adivinadas = set()
    intentos_max = len(dibujo) - 1
    errores = 0

    print(f"\n=== AHORCADO - Nivel {nivel} ===")
    print("Adivina la palabra letra por letra, o intenta la palabra completa.\n")
    
    while True:
        # Mostrar estado actual
        palabra_mostrada = " ".join([c if c in letras_adivinadas else "_" for c in palabra])
        print(dibujo[errores])
        print("Palabra: ", palabra_mostrada)
        print(f"Letras usadas: {', '.join(sorted(letras_adivinadas)) if letras_adivinadas else '(ninguna)'}")
        print(f"Intentos restantes: {intentos_max - errores}")

        # Comprobar victoria
        if all(c in letras_adivinadas for c in palabra):
            print("\n ¡Enhorabuena! Has adivinado la palabra:", palabra.upper())
            guardar_record(nivel, palabra, "GANADO", errores, intentos_max)
            break
        
        # Comprobar derrota
        if errores >= intentos_max:
            print(dibujo[errores])
            print("\nHas perdido. La palabra era:", palabra.upper())
            guardar_record(nivel, palabra, "PERDIDO", errores, intentos_max)
            break

        # entrada
        entrada = input("\nIntroduce una letra (o la palabra completa): ").strip().lower()
        
        if not entrada:
            print("  Entrada vacía. Intenta de nuevo.")
            continue
        
        # solo letra
        if len(entrada) == 1:
            if not entrada.isalpha():
                print("Por favor, introduce una letra válida.")
                continue
            if entrada in letras_adivinadas:
                print("Ya probaste esa letra.")
                continue
            if entrada in palabra:
                letras_adivinadas.add(entrada)
                print("V ¡Bien! La letra está en la palabra.")
            else:
                letras_adivinadas.add(entrada)
                errores += 1
                print("X No está en la palabra.")
        else:
            # toda la palabra
            if entrada == palabra:
                print("\n ¡Enhorabuena! Has adivinado la palabra:", palabra.upper())
                guardar_record(nivel, palabra, "GANADO", errores, intentos_max)
                break
            else:
                print(" Palabra incorrecta.")
                errores += 1


def main():
    """
    Función principal que permite jugar varias partidas.
    """
    print("""
    ╔═══════════════════════════════════╗
    ║      AHORCADO - Juego Retro       ║
    ╚═══════════════════════════════════╝
    """)
    while True:
        jugar_ahorcado()
        respuesta = input("\n¿Jugar otra vez? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n¡Hasta la proxima! ")
            break
        else:
            print("\n¡Prueba la dificultad secreta!!!!!!!!!!!!!!")

if __name__ == "__main__":
    main()