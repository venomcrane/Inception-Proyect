#!/usr/bin/env python3

import sys
import time
import random

# Caracteres digitales y animaciones
chars = ["░", "▒", "▓", "█"]  # Bloques de carga
spinners = ["|", "/", "-", "\\"]  # Animación giratoria

# Simulación de un proceso en ejecución
def hacking_loader(task="Procesando", duration=10):
    start_time = time.time()
    while time.time() - start_time < duration:
        progress = int(((time.time() - start_time) / duration) * 20)
        loading_bar = "".join(random.choices(chars, k=progress))  # Efecto glitch
        spaces = " " * (20 - progress)  # Espacios vacíos
        spinner = random.choice(spinners)  # Animación giratoria aleatoria

        sys.stdout.write(f"\r[{loading_bar}{spaces}] {spinner} {task}...")  
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write(f"\r[{'█' * 20}] ✔ {task} completado.\n")  # Finaliza el proceso

# Prueba del efecto
#hacking_loader("Fuerza bruta SSH", duration=5)

# Animación de hacking con líneas giratorias
spinners = [
    "⠁⠂⠄⡀⢀⠠⠐⠈",  # Spinner tipo Braille (estilo retro)
    "|/-\\",  # Spinner clásico
    "◐◓◑◒",  # Spinner circular
    "◴◷◶◵",  # Otro spinner circular más elegante
    "⡆⠏⠑⠡⢨⣀⣀⣀",  # Spinner en estilo binario
     "|/-\\",  # Clásico CLI
    "◐◓◑◒",  # Circular
    "◰◳◲◱",  # Cuadrado rotando
    "⡆⠏⠑⠡⢨⣀⣀⣀",  # Binario hacking
    "█▓▒░",  # Código ASCII
    "╱╲╳╲╱",  # Líneas en X
    "⠁⠂⠄⡀⢀⠠⠐⠈",  # Braille dots
    "⠋⠙⠚⠞⠖⠦⠴⠲⠳⠋",  # Hexagonal matrix
    "⣿⣷⣯⣟⡿⣿",  # Bytes de carga
    "▁▂▃▄▅▆▇█"  # Hacker Scroll
]

def hacking_spinner(task="Ejecutando proceso", duration=10, spinner_type=2):
    frames = list(spinners[spinner_type])  # Selecciona el tipo de spinner
    start_time = time.time()

    while time.time() - start_time < duration:
        for frame in frames:
            sys.stdout.write(f"\r[{frame}] {task}... ")  
            sys.stdout.flush()
            time.sleep(0.1)

    sys.stdout.write(f"\r[✔] {task} completado.\n")

# Prueba con diferentes estilos de spinner
hacking_spinner("Bypassing Authentication", duration=5, spinner_type=14)
