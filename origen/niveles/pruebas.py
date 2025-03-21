#!/usr/bin/env python3 

import os
import time
import random

# Función para generar sonidos de hacking
def sonido_hacking():
    for _ in range(2):
        os.system(f"speaker-test -t sine -f {random.randint(200, 1000)} -l 1 > /dev/null 2>&1")
        time.sleep(0.05)

# Función para error crítico
def sonido_error():
    for _ in range(3):
        os.system("speaker-test -t sine -f 900 -l 1 > /dev/null 2>&1")
        time.sleep(0.2)
        os.system("speaker-test -t sine -f 500 -l 1 > /dev/null 2>&1")
        time.sleep(0.2)

# Animación de carga
def animacion_carga():
    #efectos = ["█▒▒▒▒▒▒▒▒▒", "██▒▒▒▒▒▒▒▒", "███▒▒▒▒▒▒▒", "████▒▒▒▒▒▒", "█████▒▒▒▒▒", 
      #         "██████▒▒▒▒", "███████▒▒▒", "████████▒▒", "█████████▒", "██████████"]

    efectos = caracteres_digitales = ["◢", "◣", "◥", "◤"]
    
    print("\n[+] Accediendo al sistema...")
    for efecto in efectos:
        print(f"[\r{efecto}]", end="", flush=True)
        time.sleep(0.5)
    
    print("\n[+] Conexión establecida.")

# Simulación de ataque hacking
def hackeo():
    os.system("clear")
    print("███ HACKING EN PROGRESO ███")
    animacion_carga()
    
    print("\n[+] Descifrando datos...")
    sonido_hacking()
    
    print("\n[+] Acceso concedido. Datos comprometidos.\n")
    for _ in range(5):
        print(f"[*] Archivo: archivo_{random.randint(1000,9999)}.dat => ████▓▒░ COMPLETADO")
        time.sleep(0.3)
    
    print("\n[!] ALERTA: Seguridad detectada, activando protocolo de escape!")
    sonido_error()
    time.sleep(1)
    
    print("\n[-] Cerrando conexión...")
    animacion_carga()
    print("\n[+] Sistema fuera de peligro.")

# Iniciar nivel
animacion_carga()
#hackeo()

