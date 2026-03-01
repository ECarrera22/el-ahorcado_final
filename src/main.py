import random

# ============================
# CONFIGURACIÓN (TUPLA)
# ============================
CONFIG = (6, "v1.0")  # (intentos máximos, versión)

# ============================
# DICCIONARIO + LISTAS
# ============================
PALABRAS = {
    "Tecnologia": ["python", "robot", "internet", "inteligencia", "algoritmo"],
    "Sociedad": ["cultura", "educacion", "empleo", "globalizacion"],
    "Futuro": ["innovacion", "digital", "automatizacion", "inteligencia"]
}

# ============================
# FUNCIONES
# ============================

def mostrar_menu():
    print("\n=== JUEGO DEL AHORCADO EDUCATIVO ===")
    print("Version:", CONFIG[1])
    print("1. Jugar")
    print("2. Salir")

def seleccionar_categoria():
    print("\nCategorias disponibles:")
    for categoria in PALABRAS:
        print("-", categoria)
    categoria = input("Seleccione una categoria: ")
    return categoria

def elegir_palabra(categoria):
    return random.choice(PALABRAS[categoria])

def validar_letra(letra, usadas):
    if len(letra) != 1:
        print("Ingrese solo una letra.")
        return False
    if not letra.isalpha():
        print("Ingrese una letra valida.")
        return False
    if letra in usadas:
        print("Esa letra ya fue usada.")
        return False
    return True

def mostrar_estado(palabra, letras_correctas):
    resultado = ""
    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jugar():
    intentos = CONFIG[0]
    categoria = seleccionar_categoria()

    if categoria not in PALABRAS:
        print("Categoria invalida.")
        return

    palabra = elegir_palabra(categoria)
    letras_correctas = set()
    letras_incorrectas = set()

    while intentos > 0:
        print("\nPalabra:", mostrar_estado(palabra, letras_correctas))
        print("Intentos restantes:", intentos)
        print("Letras incorrectas:", ", ".join(letras_incorrectas) if letras_incorrectas else "Ninguna")

        letra = input("Ingrese una letra: ").lower()

        if not validar_letra(letra, letras_correctas.union(letras_incorrectas)):
            continue

        if letra in palabra:
            letras_correctas.add(letra)
            print("Correcto.")
        else:
            letras_incorrectas.add(letra)
            intentos -= 1
            print("Incorrecto.")

        # Verificar si gano
        if all(l in letras_correctas for l in palabra):
            print("\nGanaste.")
            print("La palabra era:", palabra)
            return

    print("\nPerdiste.")
    print("La palabra era:", palabra)

# ============================
# PROGRAMA PRINCIPAL
# ============================

mostrar_menu()
opcion = input("Seleccione una opcion: ")

if opcion == "1":
    jugar()
elif opcion == "2":
    print("Programa finalizado.")
else:
    print("Opcion invalida.")
