#!/usr/bin/env python3

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

# Efecto de glitch en texto
def escribir_glitch(texto, delay=0.05, color=green):
    sys.stdout.write(color)
    resultado_final = list(texto)
    texto_actual = [" "] * len(texto)
    
    for i in range(len(texto)):
        if texto[i] == " ":
            texto_actual[i] = " "
            sys.stdout.write("\r" + "".join(texto_actual))
            sys.stdout.flush()
            time.sleep(delay)
            continue

        for _ in range(random.randint(3, 8)):  # Número de glitches antes de la letra final
            texto_actual[i] = random.choice(caracteres_glitch)
            sys.stdout.write("\r" + "".join(texto_actual))
            sys.stdout.flush()
            time.sleep(delay / 2)
        
        texto_actual[i] = resultado_final[i]
        sys.stdout.write("\r" + "".join(texto_actual))
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(reset + "\n")

# Texto con pausa para generar intriga
def escribir_lento(texto, delay=0.05, color=green):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(reset + "\n")

# Pausa en negro para misterio
def pausa_negra(tiempo=3):
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(tiempo)

# Animación de puntos suspensivos
def animacion_puntos():
    for _ in range(3):
        sys.stdout.write(f"{green}.\033[0m")
        sys.stdout.flush()
        time.sleep(1)
    print()

# Fragmentos de memoria desordenados
def fragmento_memoria(fragmento, delay=0.07):
    escribir_glitch(f"{magenta}[FRAGMENTO]: {fragmento}{reset}", delay)
    time.sleep(1.5)

def nivel_desordenado():
    pistas = [
        "No puedes confiar en tus recuerdos...",
        "El tiempo no avanza en línea recta aquí...",
        "Algunos momentos parecen aleatorios, pero todos tienen un propósito...",
        "¿Recuerdas por qué empezaste esto?",
        "Debo creer que cuando mis ojos están cerrados el mundo sigue ahí."
    ]
    random.shuffle(pistas)
    for pista in pistas:
        fragmento_memoria(pista)

# Pista oculta en Base64
def nivel_base64():
    escribir_lento(f"\n{cyan}[FRAGMENTO OCULTO]: VG9kbyBlc3RhIGVzdHLDqSBjb25lY3RhZG8sIHBlcm8gY2Fkw7NuIHZlciBsb3MgbGFib3JhdG9yaW9zLg=={reset}")
    time.sleep(2)

# Mensaje final con impacto
def mensaje_final():
    escribir_lento(f"\n{magenta}[ÚLTIMO FRAGMENTO]{reset}")
    time.sleep(1)
    escribir_lento(f"{green}Cada pista te trajo hasta aquí. Pero aún falta algo.{reset}")
    escribir_lento(f"{cyan}Recuerda: el amor verdadero desafía al tiempo.{reset}")
    escribir_lento(f"{amarillo}Tienes que tomar una decisión. ¿Sigues adelante?{reset}")
    escribir_lento(f"\n{cyan}Desencripta este último mensaje para encontrar la verdad:{reset}")
    print(f"\n{green}[Base64]: aHR0cHM6Ly93d3cueW91dHViZS5jb20vZmluYWxfbWVuc2FqZV9tZW1vcnk={reset}\n")

# --- EJECUCIÓN ---

pausa_negra()  # Pausa inicial negra para intriga
interferencia()  # Simulación de interferencia/glitch

escribir_glitch("\n [Esto es una prueba]", 0.05, green)

escribir_lento(f"{cyan}========================", 0.07)
escribir_lento("  INICIANDO PROGRAMA/SUEÑO", 0.07, cyan)
escribir_lento(f"{cyan}========================\n", 0.07)

escribir_lento(f"{green}[+] Fragmentos de memoria perdidos en el tiempo...{reset}")
texto_mas_lento = lambda t, d=0.15: escribir_lento(t, d, cyan)
texto_mas_lento("¿Es un sueño, un recuerdo, o una advertencia?")
time.sleep(1)

nivel_desordenado()
time.sleep(1)
nivel_base64()
time.sleep(1)

mensaje_final()

