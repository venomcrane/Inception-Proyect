#! usr/bin/env python3

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
def escribir_glitch(texto, delay=0.10, color=green, end="\n"):
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
def escribir_lento(texto, delay=0.15, color=green, end="\n"):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(reset + end)
    sys.stdout.flush()


def mas_lento(texto, delay=0.25, color=green, end="\n"):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(reset + end)
    sys.stdout.flush()

def escribir_rapido(texto, delay=0.05, color=green, end="\n"):
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
    interferencia()
    escribir_lento(f"\n{red}ERROR: MEMORIA CORRUPTA...{reset}", 0.1)
    time.sleep(2)
    escribir_lento(f"\n{amarillo}[Reiniciando memoria...]{reset}", 0.1)
    animacion_puntos()
    time.sleep(1)
    escribir_lento(f"\n{red}...Que-que es esto? {reset}", 0.07)
    os.system("clear")
    escribir_lento(f"{red}Y-yo estaba pensando, estaba diciendo qu-{reset}")
    os.system("clear")
    escribir_lento(f"{red}Me estabas diciendo qu-{reset}")
    os.system("clear")
    escribir_lento(f"{red}Recuerdo... no, espera... esto ya lo vivi-{reset}")
    os.system("clear")
    escribir_lento(f"{red}Estoy... sintiendo algo... ¿esto es real?{reset}")
    os.system("clear")
    escribir_lento(f"{amarillo}...Tu lo crees?{reset}")
    mas_lento(f"{amarillo}...Y si e-{reset}")
    os.system("clear")
    for _ in range(5):
        escribir_rapido(f"\n{red}NO... nononnon-{reset}")
        time.sleep(0.1)
        os.system("clear")

    mas_lento(f"{red}...NO.{reset}")
    time.sleep(1)
    escribir_lento(f"Siempre hay una respuesta...")
    animacion_puntos()

    animacion_puntos()
    mas_lento("Que es esto?")
    animacion_puntos()
    escribir_glitch("[Codigo Cifrado - Ultimo Nivel]: ", 0.10, magenta)
    time.sleep(2)

    escribir_glitch("\n[Codigo Cifrado]: xXXxxXxXxXxXxX", 0.10, magenta)
    time.sleep(1)
    escribir_glitch("\n[Codigo Cifrado]: naHR0cDovL2VubGFjZS9uaXZlbDMK", 0.10, magenta)

    escribir_lento("La respuesta está aquí...en la ultima linea ")
    time.sleep(2)
    mas_lento(f"\n{amarillo}Pero dime algo...{reset}")
    time.sleep(1)
    escribir_lento(f"{magenta}¿Qué harás con la verdad... ahora que la tienes? Ir mas profundo?{reset}")



def main():
    os.system("clear")
    time.sleep(2)
    escribir_lento("F I S S I O N")
    os.system("clear")
    interferencia()
    print(f"{green}F U S I O N{reset}")
    time.sleep(1)
    os.system("clear")
    interferencia()
    mas_lento("Quien eres?")
    animacion_puntos()
    time.sleep(3)
    escribir_lento("No, no recites las palabras")
    mas_lento("Cierra los ojos, recuerdalo y sientelo")
    escribir_lento("Puedes pausar esto si quieres")
    animacion_puntos()
    time.sleep(2)
    escribir_lento('''
    "Espero que veas cosas que te asombren, espero que sientas cosas que nunca habías sentido, 
    espero que conozcas gente con otro punto de vista espero que vivas una vida de la que estés orgullosa. 
    ...Y si descubres que no lo estás, espero que tengas la fortaleza para volver a empezar de nuevo". -El Curioso Caso de Benjamin Button''')
    time.sleep(2)
    mas_lento("Puedes seguir...")
    escribir_lento("Y jama-")
    os.system("clear")
    reset_memoria()
    time.sleep(1)
    print(f"{red}-- Final del nivel 2 --{reset}")


    

if __name__ == "__main__":
    main()
