#!/usr/bin/env python3 

import time
import sys
import random

spinner = ["[◢]", "[◣]", "[◤]", "[◥]"]

print("\n[+] Accediendo al sistema...")

for _ in range(20):  # Número de vueltas
    for frame in spinner:
        sys.stdout.write(f"\r{frame}")  # Sobrescribe en la misma línea
        sys.stdout.flush()
        time.sleep(0.1)


spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

for _ in range(20):
    for frame in spinner:
        sys.stdout.write(f"\r{frame} Accediendo al sistema...")  
        sys.stdout.flush()
        time.sleep(0.1)


spinner = ["|", "/", "-", "\\"]
for _ in range(20):
    for frame in spinner:
        sys.stdout.write(f"\r{frame}")
        sys.stdout.flush()
        time.sleep(0.1)

bar_length = 20
for i in range(bar_length + 1):
    sys.stdout.write(f"\r[{'█' * i}{' ' * (bar_length - i)}] {i*5}%")
    sys.stdout.flush()
    time.sleep(0.1)
print("\n[✔] Completado.")

chars = ["█", "▓", "▒", "░"]
for _ in range(10):
    line = "".join(random.choice(chars) for _ in range(30))
    sys.stdout.write(f"\r{line}")
    sys.stdout.flush()
    time.sleep(0.1)
print("\n")


print("\nCargando", end="")
for _ in range(10):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.2)
print("\n[✔] Listo.")



for _ in range(50):
    text = "".join(random.choice(chars) for _ in range(20))
    sys.stdout.write(f"\r{text}")
    sys.stdout.flush()
    time.sleep(0.05)
print("\n[✔] Hack completado.")


spinner = ["◴", "◷", "◶", "◵"]

for _ in range(20):
    for frame in spinner:
        sys.stdout.write(f"\r{frame}")
        sys.stdout.flush()
        time.sleep(0.1)

stars = ["✦", "✧", "★", "☆", "✪"]
for _ in range(30):
    text = "".join(random.choice(stars) for _ in range(20))
    sys.stdout.write(f"\r{text}")
    sys.stdout.flush()
    time.sleep(0.1)
print("\n[✔] Simulación completada.")
