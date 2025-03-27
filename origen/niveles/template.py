#! usr/bin/env python3

import time
import sys
import random
import os
import signal

# Colores ANSI para efectos visuales
green = "\033[92m"
cyan = "\033[96m"
rojo = "\033[91m"
amarillo = "\033[93m"
magenta = "\033[95m"
reset = "\033[0m"
bold = "\033[1m"

# Manejo de Ctrl+C para salida dramática
def leaving(sig, frame):
    print(f"\n\n{rojo}[!] TERMINANDO PROCESO ...\n{reset}")
    sys.exit(1)

signal.signal(signal.SIGINT, leaving)

# Caracteres aleatorios para glitch
caracteres_glitch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Simulación de interferencia
def interferencia():
    for _ in range(5):
        sys.stdout.write(random.choice(["█", "░", "▒", "▓"]) * 40 + "\n")
        sys.stdout.flush()
        time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')

# Efecto de texto glitch
def escribir_glitch(texto, delay=0.10, color=green, end="\n"):
    """Muestra un efecto de letras aleatorias que se convierten en la frase final. ⭐"""
    sys.stdout.write(color)
    sys.stdout.flush()
    
    resultado_final = list(texto)  # Convertir el texto en lista
    texto_actual = [" "] * len(texto)  # Crear una lista vacía del mismo tamaño

    for i in range(len(texto)):  # Iterar por cada letra
        if texto[i] == " ":  # Mantener espacios sin efecto glitch
            texto_actual[i] = " "
            sys.stdout.write("\r" + "".join(texto_actual))
            sys.stdout.flush()
            time.sleep(delay)
            continue
        
        for _ in range(random.randint(3, 8)):  # Número de iteraciones glitch
            texto_actual[i] = random.choice(caracteres_glitch)  # Mostrar letras aleatorias
            sys.stdout.write("\r" + "".join(texto_actual))
            sys.stdout.flush()
            time.sleep(delay / 2)
        
        texto_actual[i] = resultado_final[i]  # Mostrar la letra final correcta
        sys.stdout.write("\r" + "".join(texto_actual))
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(reset + end)  # Aquí nos aseguramos de que `end` funcione bien
    sys.stdout.flush()



# Texto con pausa para generar intriga
def escribir_lento(texto, delay=0.10, color=green, end="\n"):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(reset + end)
    sys.stdout.flush()


def mas_lento(texto, delay=0.25, color=green, end="\n"):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(reset + end)
    sys.stdout.flush()



# Animación de puntos suspensivos
def animacion_puntos():
    for _ in range(3):
        sys.stdout.write(f"{green}.{reset}")
        sys.stdout.flush()
        time.sleep(1)
    print()


def main():
    os.system("clear")
    
    

if __name__ == "__main__":
    main()
