#!/usr/bin/env python3

import time
import sys
import random
import os
import signal

# Colores ANSI para estética Matrix
green = "\033[92m"
cyan = "\033[96m"
rojo = "\033[91m"
amarillo = "\033[93m"
magenta = "\033[95m"
reset = "\033[0m"

# Manejo de Ctrl+C para cierre dramático
def leaving(sig, frame):
    print(f"\n\n{rojo}[!] TERMINANDO PROCESO ...\n{reset}")
    sys.exit(1)

signal.signal(signal.SIGINT, leaving)

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


# Limpia pantalla antes de comenzar
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Efecto de máquina de escribir con color
def escribir_lento(texto, delay=0.05, color=green):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(reset + "\n")

# Animación de puntos suspensivos
def animacion_puntos():
    for _ in range(3):
        sys.stdout.write(f"{green}.\033[0m")
        sys.stdout.flush()
        time.sleep(1)
    print()

# Efecto de "código cargando" al estilo Matrix
def efecto_matrix():
    caracteres = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(15):  # Cantidad de líneas
        linea = "".join(random.choice(caracteres) for _ in range(40))
        print(f"{green}{linea}{reset}")
        time.sleep(0.1)
    print("\n")

# Animación de inicio
def animacion_inicio():
    print(f"{cyan}========================")
    escribir_lento("  INICIANDO PROGRAMA/SUEÑO", 0.07, cyan)
    print(f"{cyan}========================\n")
    time.sleep(1)
    efecto_matrix()
    escribir_lento("[+] CARGANDO FRAGMENTOS DE MEMORIA ...", 0.05, amarillo)
    animacion_puntos()
    time.sleep(1)

# Fragmentos de memoria desordenados
def fragmento_memoria(fragmento, delay=0.07):
    escribir_lento(f"{magenta}[FRAGMENTO]: {fragmento}{reset}", delay)
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
    escribir_lento(f"\n{cyan}[FRAGMENTO OCULTO]: VG9kbyBlc3RhIGVzdHLDqSBjb25lY3RhZG8sIHBlcm8gY2Fkw7NuIHZlciBsb3MgbGFib3JhdG9yaW9zLg=={reset}")
    time.sleep(2)

# Efecto de memoria reiniciándose (como un glitch en la simulación)
def reset_memoria():
    escribir_lento(f"\n{rojo}ERROR: MEMORIA CORRUPTA...{reset}", 0.1)
    time.sleep(2)
    escribir_lento(f"\n{amarillo}[Reiniciando memoria...]{reset}", 0.1)
    animacion_puntos()
    time.sleep(1)
    escribir_lento(f"\n{green}...Vuelve al principio. ¿Qué ignoraste?{reset}", 0.07)

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
limpiar_pantalla()

#escribir_glitch("\n [Esto es una prueba]",0.05,green)

animacion_inicio()
escribir_lento(f"{green}[+] Fragmentos de memoria perdidos en el tiempo...{reset}")
texto_mas_lento = lambda t, d=0.15: escribir_lento(t, d, cyan)  # Función rápida para texto más lento
texto_mas_lento("¿Es un sueño, un recuerdo, o una advertencia?")
time.sleep(1)

nivel_desordenado()
time.sleep(1)
nivel_base64()
time.sleep(1)

# Giro inesperado en la narrativa (estilo Memento)
reset_memoria()
time.sleep(2)

mensaje_final()

