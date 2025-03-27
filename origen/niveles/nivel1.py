#!/usr/bin/env python3

import time
import sys
import random
import os
import signal

# Colores ANSI para efectos visuales
green = "\033[92m"
cyan = "\033[96m"
red = "\033[91m"
amarillo = "\033[93m"
magenta = "\033[95m"
reset = "\033[0m"
bold = "\033[1m"

# Manejo de Ctrl+C para salida dramática
def leaving(sig, frame):
    print(f"\n\n{red}[!] TERMINANDO PROCESO ...\n{reset}")
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
def escribir_glitch(texto, delay=0.25, color=green, end="\n"):
    """Muestra un efecto de letras aleatorias que se convierten en la frase final."""
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
def escribir_lento(texto, delay=0.05, color=green, end="\n"):
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

# Efecto de memoria reiniciándose (como un glitch en la simulación)
def reset_memoria():
    escribir_lento(f"\n{rojo}ERROR: MEMORIA CORRUPTA...{reset}", 0.1)
    time.sleep(2)
    escribir_lento(f"\n{amarillo}[Reiniciando memoria...]{reset}", 0.1)
    animacion_puntos()
    time.sleep(1)
    escribir_lento(f"\n{green}...Vuelve al principio. ¿Qué ignoraste?{reset}", 0.07)

# Fragmentos de memoria desordenados
def fragmento_memoria(fragmento, delay=0.07):
    print(f"{magenta}[FRAGMENTO]: {fragmento}{reset}")
    time.sleep(3)

def nivel_desordenado():
    pistas = [
        "Nunca olvides tus recuerdos aunque los demás digan lo contrario...",
        "El tiempo... esa palabra...",
        "Sin el tiempo los arboles no serian fuertes no crees?",
        "Y sin el tiempo serian tan breves y efimeros como las hojas que se lleva el viento",
        "El mundo no desaparece cuando cierras los ojos... o si?",
        "Contigo puedo ser yo mismo..."
    ]
    for pista in pistas:
        fragmento_memoria(pista)

# Pista oculta en Base64
def nivel_base64(): 
    escribir_glitch("[FRAGMENTO OCULTO]: TWUgcmVjb3JkYXJhcz8uLi4K", 0.07, green, end="\n")
    time.sleep(2)



# Mensaje final con impacto
def mensaje_final():
    escribir_lento(f"\n{magenta}[ÚLTIMO FRAGMENTO]: {reset}", 0.05, end="")
    time.sleep(1)
    escribir_lento(f"{green}Cada pista te trajo hasta aquí. Pero aún falta algo.{reset}")
    escribir_lento(f"{cyan}...{reset}")
    escribir_lento(f"{amarillo}La vida esta llena de decisiones, la mas minima puede cambiarlo todo{reset}")
    escribir_lento(f"{amarillo}Una sola decision lo cambio todo...{reset}")
    time.sleep(2)
    escribir_lento(f"\n{cyan}La verdad esta cerca: {reset}")
    escribir_glitch("aHR0cHM6Ly93d3cueW91dHViZS5jb20vZmluYWxfbWVuc2FqZV9tZW1vcnk=")

# --- EJECUCIÓN ---
print(f"{cyan}========================")
escribir_lento("  INICIANDO PROGRAMA", 0.07, cyan)
print(f"{cyan}========================")

escribir_lento(f"{green}[+] Fragmentos de memoria perdidos en el tiempo...{reset}")
texto_mas_lento = lambda t, d=0.15: escribir_lento(t, d, cyan)
texto_mas_lento("¿Es un sueño o un recuerdo?")
time.sleep(1)

nivel_desordenado()
time.sleep(1)
nivel_base64()
time.sleep(1)
mensaje_final()
print(f"{red}\t\t\t--- Fin del nivel 1 --- {reset}")
