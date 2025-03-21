#!/usr/bin/env python3

import time
import sys
import random
import os
import signal

# Manejo de Ctrl+C para un cierre dramático
def leaving(sig, frame):
    print("\n\n\033[91m[!] El sueño se desvanece...\033[0m\n")
    sys.exit(1)

signal.signal(signal.SIGINT, leaving)

# Limpia la pantalla antes de comenzar
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Efecto de máquina de escribir con colores
def escribir_lento(texto, delay=0.05, color="\033[92m"):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")  # Restablecer color y hacer un salto de línea

# Versión más lenta para generar suspenso
def texto_mas_lento(texto, delay=0.15, color="\033[96m"):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

# Animación de puntos suspensivos
def animacion_puntos():
    for _ in range(3):
        sys.stdout.write("\033[92m.\033[0m")
        sys.stdout.flush()
        time.sleep(1)
    print()

# Fragmentos desordenados estilo "Memento"
def fragmento_memoria(fragmento, delay=0.07):
    escribir_lento(f"\033[93m[Fragmento]: {fragmento}\033[0m", delay)
    time.sleep(1.5)

def nivel_desordenado():
    pistas = [
        "No puedes confiar en tus recuerdos.",
        "Lo que crees que pasó... ¿realmente sucedió así?",
        "El tiempo no avanza en línea recta aquí.",
        "Algunos momentos parecen aleatorios, pero todos tienen un propósito.",
        "No olvides por qué empezaste a descifrar esto."
    ]
    random.shuffle(pistas)
    for pista in pistas:
        fragmento_memoria(pista)

# Pista oculta en Base64
def nivel_base64():
    escribir_lento("\n\033[94m[Fragmento oculto]: VG9kbyBlc3RhIGVzdHLDqSBjb25lY3RhZG8sIHBlcm8gY2Fkw7NuIHZlciBsb3MgbGFib3JhdG9yaW9zLg==\033[0m")
    time.sleep(2)

# Efecto de memoria reiniciándose (sorpresa estilo "Memento")
def reset_memoria():
    escribir_lento("\n\033[91mAlgo no está bien... ¿qué olvidaste?\033[0m", 0.1)
    time.sleep(2)
    escribir_lento("\n\033[93m[Reiniciando memoria...]\033[0m", 0.1)
    animacion_puntos()
    time.sleep(1)
    escribir_lento("\n\033[92m...Vuelve al principio. ¿Qué ignoraste?\033[0m", 0.07)

# Mensaje final con impacto
def mensaje_final():
    escribir_lento("\n\033[95m[Último Fragmento]\033[0m")
    time.sleep(1)
    escribir_lento("\033[92mCada pista te trajo hasta aquí. Pero aún falta algo.\033[0m")
    escribir_lento("\033[96mRecuerda: el amor verdadero desafía al tiempo.\033[0m")
    escribir_lento("\033[93mTienes que tomar una decisión. ¿Sigues adelante?\033[0m")
    escribir_lento("\n\033[94mDesencripta este último mensaje para encontrar la verdad:\033[0m")
    print("\n\033[92m[Base64]: aHR0cHM6Ly93d3cueW91dHViZS5jb20vZmluYWxfbWVuc2FqZV9tZW1vcnk=\033[0m\n")

# --- EJECUCIÓN ---
limpiar_pantalla()
texto_mas_lento("\n\033[91m[Inicio del Sueño]\033[0m", 0.1)
escribir_lento("\033[92m[+] Fragmentos de memoria perdidos en el tiempo...\033[0m")
texto_mas_lento("\033[96m¿Es un sueño, un recuerdo, o una advertencia?\033[0m")
time.sleep(1)

nivel_desordenado()
time.sleep(1)
nivel_base64()
time.sleep(1)

# Un giro inesperado en la narrativa (como *Memento*)
reset_memoria()
time.sleep(2)

mensaje_final()

