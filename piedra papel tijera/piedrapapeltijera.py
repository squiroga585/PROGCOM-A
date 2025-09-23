import tkinter as tk
from tkinter import messagebox
import random
import pygame

# Ventana principal
root = tk.Tk()
root.title("Piedra papel y tijera")

# Elecciones
choices = ["Piedra", "Papel", "Tijera"]

# Funcion para determinar ganador
def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""
    if user_choice == computer_choice:
        result = "Empate!"
    elif (user_choice == "Piedra" and computer_choice == "Tijera") or \
         (user_choice == "Papel" and computer_choice == "Piedra") or \
         (user_choice == "Tijera" and computer_choice == "Papel"):
        result = "Ganaste!"
    else:
        result = "La computadora gana!"
    messagebox.showinfo("Resultado", f"Elejiste {user_choice}\nComputadora eligio {computer_choice}\n{result}")

# Layout
tk.Label(root, text="Elije:").pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

for choice in choices:
    tk.Button(btn_frame, text=choice, width=10, command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=5)


Imagenes_juego = []
Imagenes_jurgo = ["imagenes/Piedra_1.jpg","imagenes/Piedra_2.jpg", "imagenes/Papel_1.jpg", "imagenes/Papel_2.jpg" "imagenes/Tijera_1.jpg", "imagenes/Tijera_2.jpg"]

root.mainloop()