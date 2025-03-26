#!/usr/bin/env python3

import time
import sys
import random
import os
import signal

# Colores ANSI para estética hacker
green = "\033[92m"
cyan = "\033[96m"
rojo = "\033[91m"
amarillo = "\033[93m"
magenta = "\033[95m"
reset = "\033[0m"

# Caracteres aleatorios para el efecto glitch
caracteres_glitch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Efecto glitch de desencriptación en tiempo real
def escribir_glitch(texto, delay=0.05, color=green):
    """Muestra un efecto de letras aleatorias que se convierten en la frase final."""
    sys.stdout.write(color)
    
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

    sys.stdout.write(reset + "\n")  # Resetear color y hacer salto de línea

# Pista oculta en Base64 con efecto glitch
def nivel_base64():
    print(f"{magenta}[FRAGMENTO OCULTO]:{reset} ", end="")  # No genera salto de línea
    escribir_glitch("TWUgcmVjb3JkYXJhcz8uLi4K", 0.07, green)
    time.sleep(2)


nivel_base64()
