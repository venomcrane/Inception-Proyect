#!/usr/bin/python env 

import time
import sys
import random
import requests
import signal 
import os

def leaving(sig,frame):
    #print("\n\n[!]Aborting")
    print("\n\n\033[91m[!] Aborting ...\n\033[0m")
    sys.exit(1)

#Ctrl+C 
signal.signal(signal.SIGINT, leaving)

def escribir_lento(texto, delay=0.05):
    """Escribe texto con efecto de máquina de escribir."""
    verde = "\033[92m"
    reset = "\033[0m"

    for char in texto:
        sys.stdout.write(verde + char + reset)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def texto_mas_lento(texto, delay=0.20):
    """Escribe el texto aun mas lento"""
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

def fragmento_memoria(fragmento):
    """Muestra fragmentos desordenados con efecto especial."""
    escribir_lento(f"[Fragmento]: {fragmento}")
    time.sleep(2)

def nivel_desordenado():
    """Simula un nivel desordenado de narrativa."""
    pistas = [
        "En un sueño, los recuerdos se desvanecen como arena entre los dedos.",
        "Las emociones no son lineales; fluyen y chocan como olas.",
        "Piensa en cada momento: ¿qué conecta todo esto?",
        "No olvides lo que viste, incluso si parece sin sentido ahora.",
        "Al final, todo será claro. Solo sigue las pistas."
    ]
    random.shuffle(pistas)
    for pista in pistas:
        fragmento_memoria(pista)

def nivel_base64():
    """Incluye una pista oculta en Base64."""
    escribir_lento("\033[96m[Fragmento oculto]: VG9kbyBlc3RhIGVzdHLDqSBjb25lY3RhZG8sIHBlcm8gY2Fkw7NuIHZlciBsb3MgbGFib3JhdG9yaW9zLg==\033[0m")
    time.sleep(2)

def mensaje_final():
    """Desenlace con la decisión final."""
    escribir_lento("\n[Último Fragmento]")
    time.sleep(1)
    escribir_lento("Cada pista, cada recuerdo, te trajo hasta aquí.")
    escribir_lento("Ahora: ¿qué significa todo esto?")
    escribir_lento("Desencripta este último mensaje para descubrir la verdad:")
    print("\033[92m[Base64]: aHR0cHM6Ly93d3cueW91dHViZS5jb20vZmluYWxfbWVuc2FqZV9tZW1vcnk=\033[0m")

# Ejecución
os.system('clear')
texto_mas_lento("\n[Inicio del Sueño]")
escribir_lento("[+] Los fragmentos de memoria son como espejos rotos.")
texto_mas_lento("No tienen orden... Pero el tiempo avanza a una sola direccion.")
time.sleep(1)
nivel_desordenado()
time.sleep(1)
nivel_base64()
time.sleep(1)
mensaje_final()

