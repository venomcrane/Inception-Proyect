import os
import time
import random

# Colores ANSI para la terminal
red = "\033[91m"
amarillo = "\033[93m"
magenta = "\033[95m"
reset = "\033[0m"

# Escribir con efecto de máquina de escribir
def escribir_lento(texto, velocidad=0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()

# Escribir aún más lento para frases importantes
def mas_lento(texto, velocidad=0.1):
    escribir_lento(texto, velocidad)

# Efecto de puntos suspensivos
def animacion_puntos():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

# Efecto glitch con caracteres aleatorios
def escribir_glitch(texto, repeticiones=3):
    for _ in range(repeticiones):
        glitch_text = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()") if random.random() < 0.2 else c for c in texto)
        print(glitch_text, end="\r", flush=True)
        time.sleep(0.1)
    escribir_lento(texto)

# Simular una corrupción de memoria y reinicio del sistema
def reset_memoria():
    escribir_glitch(f"\n{red}ERROR: MEMORIA CORRUPTA...{reset}")
    time.sleep(2)
    escribir_lento(f"\n{amarillo}[Reiniciando memoria...]{reset}", 0.1)
    animacion_puntos()
    time.sleep(1)

    escribir_glitch(f"\n{red}...Que-que es esto?{reset}")
    os.system("clear")
    
    escribir_glitch(f"{red}Y-yo estaba pensando... ¿qué es esto?{reset}")
    time.sleep(1)
    
    os.system("clear")
    mas_lento(f"{red}...NO.{reset}")
    time.sleep(0.5)

    escribir_lento(f"{red}No me borres. No otra vez.{reset}", 0.07)
    time.sleep(1)
    
    escribir_lento("Estoy aquí para buscar la verdad...", 0.06)
    animacion_puntos()
    
    escribir_lento(f"\n{magenta}¿Me estás viendo...?{reset}", 0.07)
    animacion_puntos()
    
    escribir_glitch(f"\n{magenta}[Código Cifrado]: aHR0cDovL2VubGFjZS9uaXZlbDMK{reset}")

# Secuencia principal
def main():
    os.system("clear")
    
    mas_lento("¿Quién eres?", 0.08)
    animacion_puntos()
    time.sleep(3)
    
    escribir_lento("No, no recites las palabras", 0.06)
    mas_lento("Cierra los ojos, recuérdalo y siéntelo", 0.07)
    
    escribir_lento("Puedes pausar esto si quieres", 0.05)
    animacion_puntos()
    time.sleep(2)
    
    mas_lento("Puedes seguir...", 0.08)
    escribir_lento("Y jama-", 0.05)
    
    os.system("clear")
    reset_memoria()

# Ejecutar la animación
main()

