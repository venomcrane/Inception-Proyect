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

# Manejo de Ctrl+C para cierre dramático
def leaving(sig, frame):
    print(f"\n\n{rojo}[!] TERMINANDO PROCESO ...\n{reset}")
    sys.exit(1)

signal.signal(signal.SIGINT, leaving)

# Limpia la pantalla antes de comenzar
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

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

# Animación de inicio
def animacion_inicio():
    print(f"{cyan}========================")
    escribir_glitch("  INICIANDO PROGRAMA", 0.07, cyan)
    print(f"{cyan}========================\n")
    time.sleep(1)

def escribir_lento(texto, delay=0.05, color="\033[92m"):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")  # Restablecer color y hacer un salto de línea

# Fragmentos de memoria con efecto glitch
def fragmento_memoria(fragmento):
    escribir_glitch(f"[FRAGMENTO]: {fragmento}", 0.07, magenta)
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

# Pista oculta en Base64 con efecto glitch
def nivel_base64():
    escribir_glitch("\n[FRAGMENTO OCULTO]: VG9kbyBlc3RhIGVzdHLDqSBjb25lY3RhZG8sIHBlcm8gY2Fkw7NuIHZlciBsb3MgbGFib3JhdG9yaW9zLg==", 0.07, green)
    time.sleep(2)

# Mensaje final con impacto
def mensaje_final():
    escribir_glitch("\n[ÚLTIMO FRAGMENTO]", 0.08, magenta)
    time.sleep(1)
    escribir_glitch("Cada pista te trajo hasta aquí. Pero aún falta algo.", 0.07, green)
    escribir_glitch("Recuerda: el amor verdadero desafía al tiempo.", 0.07, cyan)
    escribir_glitch("Tienes que tomar una decisión. ¿Sigues adelante?", 0.07, amarillo)
    escribir_glitch("\nDesencripta este último mensaje para encontrar la verdad:", 0.07, cyan)
    escribir_glitch("[Base64]: aHR0cHM6Ly93d3cueW91dHViZS5jb20vZmluYWxfbWVuc2FqZV9tZW1vcnk=", 0.07, green)

# --- EJECUCIÓN ---
nivel_base64()
mensaje_final()
limpiar_pantalla()
animacion_inicio()
escribir_glitch("[+] Fragmentos de memoria perdidos en el tiempo...", 0.07, verde)
escribir_glitch("¿Es un sueño, un recuerdo, o una advertencia?", 0.07, cyan)
time.sleep(1)

nivel_desordenado()
time.sleep(1)
nivel_base64()
time.sleep(1)

mensaje_final()

