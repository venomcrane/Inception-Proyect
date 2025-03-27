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

def clear():
    os.system("clear")

def main():
    clear()
    print((f"{cyan}Te quiero mucho{reset} " * 500))
    escribir_lento("> Asi que quisiste llegar a lo mas profundo?", 0.10, amarillo)
    time.sleep(1)
    escribir_lento("> Llegare hasta donde sea necesario...")
    time.sleep(2)
    clear()
    escribir_lento("Porque lo cierto es que la verdad siempre estuvo ahi... siempre estuvo aqui")
    clear()
    interferencia()
    interferencia()
    interferencia()
    print(f"{red}==== ERROR: Corrupción de memoria detectada ====")
    time.sleep(1)
    print(f"{red}...Intentando recuperacion....{reset}")
    animacion_puntos()
    time.sleep(2)
    clear()
    print(f"{cyan}[::] Sistema Restablecido [::] {reset}")
    time.sleep(2)
    clear()
    print(f"{cyan}=========================[::] LEVEL 3 - GROUND ZERO [::]====================================")
    escribir_lento('''
    "Espero que veas cosas que te asombren, espero que sientas cosas que nunca habías sentido, 
    espero que conozcas gente con otro punto de vista espero que vivas una vida de la que estés orgullosa. 
    ...Y si descubres que no lo estás, espero que tengas la fortaleza para volver a empezar de nuevo". -El Curioso Caso de Benjamin Button''')
    animacion_puntos()
    animacion_puntos()
    escribir_lento("Porque lo que más quiero es que seas feliz")
    time.sleep(1)
    escribir_lento("No hay nada como tu sonrisa...")
    time.sleep(0.5)
    escribir_lento("...Ni como tus risas")
    time.sleep(0.7)
    escribir_lento("...Ni como tu forma de ser")
    time.sleep(1)
    escribir_lento("No hay nada como tus mejillitas cuando estás contenta...")
    time.sleep(1)
    escribir_lento("...Cuando estás nerviosa.")
    time.sleep(2)
    escribir_lento("No hay nada ni nadie como tu")
    time.sleep(1)
    escribir_lento("Lo senti y lo supe desde el primer dia...")
    escribir_lento("Recuerdo con nitides cada detalle...")
    escribir_lento("Hay cosas que el tiempo no puede borrar")
    escribir_lento("No porque la memoria las guarde,\nSino porque el alma las reconoce")
    animacion_puntos()
    escribir_lento("El sonido de tu risa")
    escribir_lento("El instante en el que nuestras miradas se cruzaron por primera vez")
    escribir_lento("...La certeza de que eres tu")
    animacion_puntos()
    escribir_lento(f"{amarillo}Si el tiempo nos hace esperar{reset}")
    escribir_lento(f"{amarillo}Si la distancia nos separa{reset}")
    escribir_lento(f"{amarillo}Si las dudas intentan colarse entre nosotros{reset}")
    escribir_lento(f"{cyan}Siempre estaras en lo mas profundo de mi corazon y se que en el momento correto, en el lugar correcto en esta vida... Seras tu\nToda una vida. {reset}")
    escribir_lento("El tiempo nos pondra a prueba, la distancia tambien, pero lo real y genuino siempre se fortalezera porque el amor nunca falla")
    escribir_lento("Y si, sabemos lo que siente el otro (y es algo muy bonito) pero no quiero que sea algo como de 'espera' sino algo bonito, divertido jaja muy divertido, que nos divirtamos y sigamos adelante")
    time.sleep(2)
    escribir_lento("Gracias por todo...mejillitas <3")
    time.sleep(1)
    escribir_glitch("[Mensaje]: ")
    print((f"{cyan}Te quiero mucho{reset} " * 500))
    time.sleep(3)
    animacion_puntos()
    escribir_glitch("Para toda una vida")
    time.sleep(2)
    clear()
    escribir_rapido("[::] Conexion Finalizada [::]",0.05, red)
    time.sleep(2)
    print(f"{red}==============================[::] FIN DEL PROGRAMA [::]================================")
    animacion_puntos()
    escribir_glitch("[FINAL/INICIO SECRETO]: ZmluYWwgc2VjcmV0bwo= ")
    

if __name__ == "__main__":
    main()
