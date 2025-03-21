import time
import sys

# Funciones reutilizables
def escribir_lento(texto, delay=0.05):
    """Escribe texto con efecto de máquina de escribir."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animacion_puntos():
    """Animación de puntos suspensivos."""
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()

# Narrativa
def teoria_fision():
    escribir_lento("Teoría de la Fisión Emocional:")
    time.sleep(1)
    escribir_lento("Las emociones son como átomos.")
    escribir_lento("Cargadas de energía...")
    escribir_lento("... y capaces de liberar una fuerza incontrolable.")
    animacion_puntos()
    escribir_lento("Cada interacción es un intercambio de energía.")
    escribir_lento("Y cada decisión, una reacción en cadena.")
    time.sleep(2)

def nivel_uno():
    escribir_lento("\n[Nivel 1: La Inestabilidad del Núcleo]")
    time.sleep(1)
    escribir_lento("Imagina un núcleo emocional: nosotros.")
    escribir_lento("A veces estable, otras veces frágil.")
    escribir_lento("¿Qué pasa cuando introducimos algo inesperado?")
    animacion_puntos()
    escribir_lento("Solo tú puedes decidir si este núcleo se colapsa...")
    escribir_lento("... o libera una energía que trasciende.")

def nivel_dos():
    escribir_lento("\n[Nivel 2: La Reacción en Cadena]")
    time.sleep(1)
    escribir_lento("Una pequeña decisión...")
    escribir_lento("... puede desencadenar una reacción en cadena.")
    escribir_lento("Piensa en cómo llegamos aquí.")
    escribir_lento("Cada palabra, cada gesto.")
    animacion_puntos()
    escribir_lento("Estamos en un punto crítico.")
    time.sleep(2)

def nivel_final():
    escribir_lento("\n[El Plutonio Emocional]")
    time.sleep(1)
    escribir_lento("Aquí está la chispa.")
    escribir_lento("La decisión final está en tus manos.")
    escribir_lento("Lo que suceda después...")
    escribir_lento("... dependerá de tu elección.")
    time.sleep(2)
    escribir_lento("¿Estás lista para desencadenar la fisión emocional?")
    animacion_puntos()
    escribir_lento("Descifra el siguiente enlace para encontrar la chispa final:")
    print("\n[Base64]: aHR0cHM6Ly93d3cueW91dHViZS5jb20vZXhwbG9zaW9uX3ZpZGVv")

# Ejecución
teoria_fision()
nivel_uno()
nivel_dos()
nivel_final()

