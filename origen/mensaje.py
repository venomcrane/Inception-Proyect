#!/usr/bin/env python3

import time 
import sys
import random 
import os 
import signal 

# Colores ANSI para estética hacker
green = "\033[92m"
cyan = "\033[96m"
red = "\033[91m"
amarillo = "\033[93m"
magenta = "\033[95m"
reset = "\033[0m"

# Caracteres aleatorios para el efecto glitch
caracteres_glitch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Manejo de Ctrl+C para cierre dramático
def leaving(sig, frame):
    print(f"\n\n{red}[!] TERMINANDO PROCESO ...\n{reset}")
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


def escribir_lento(texto, delay=0.05, color="\033[92m"):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")  # Restablecer color y hacer un salto de línea

def mas_lento(texto, delay=0.20, color="\033[92m"):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")  # Restablecer color y hacer un salto de línea



# Animación de inicio
def animacion_inicio():
    print(f"{cyan}========================")
    escribir_lento("  INICIANDO PROGRAMA", 0.07, cyan)
    print(f"{cyan}========================\n")
    time.sleep(1)

def fragmento_memoria(fragmento):
    print("[FRAGMENTO]:", end=' ')
    escribir_lento(f"{fragmento}", 0.07, green)
    time.sleep(1.5)


def nivel_desordenado():
    pistas = [
        "EL tiempo cuando dormimos es diferente.. pero las emociones siempre son reales",
        "Como sabes que no estas viviendo un recuerdo en este momento?",
        "Esperas un tren... un tren que te llevara muy lejos...",
        "Las estrellas que ves hoy brillaron han brillado por siglos. La distancia no significa ausencia.",
        "No olvides por qué empezaste a descifrar esto.",
        "El amor que es real, el tiempo solo lo refina, nunca lo debilita"
    ]

    random.shuffle(pistas)
    for pista in pistas:
        fragmento_memoria(pista)

# Pista oculta en Base64 con efecto glitch
def nivel_base64():
    escribir_glitch("[FRAGMENTO OCULTO]: TnVuY2EgZGVqZXMgZGUgc2VyIHR1IG1pc21hLCBtZWppbGxhcyByb3NhZGl0YXMK", 0.07, magenta)
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



#--- EJECUCION ---
limpiar_pantalla()
animacion_inicio()
escribir_lento("[+] CARGANDO FRAGMENTOS DE MEMORIA...",0.07, cyan)
mas_lento("...",0.07, green)
escribir_lento("[+] Los Fragmentos de Memoria son como espejos rotos", 0.07, green)
time.sleep(1)
escribir_lento("[+] No tienen orden pero avanzan a una sola direccion")
mas_lento(f"[+] ¿Es un sueño, un recuerdo, o... algo mas?")
time.sleep(1)

nivel_desordenado()
print()
time.sleep(1)
nivel_base64()
print()
time.sleep(1)
escribir_lento("[!] ERROR: MEMORIA CORRUPTA", 0.07, red)
print()
time.sleep(2)
limpiar_pantalla()
mas_lento("...")
print()
escribir_lento("[Reiniciando memoria]")
mas_lento("...")

