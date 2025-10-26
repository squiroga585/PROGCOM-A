import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("TIC-TAC-TOE")
        self.tablero = [" " for _ in range(9)]
        self.turno = "X"  
        self.bot = "O"    
        self.crear_botones()

    def crear_botones(self):
        self.botones = []
        for i in range(9):
            boton = tk.Button(self.master, text=" ", font=('Arial', 20), width=5, height=2,
                              command=lambda i=i: self.jugar(i))
            boton.grid(row=i // 3, column=i % 3)
            self.botones.append(boton)

    def jugar(self, i):
        if self.tablero[i] == " ":
            self.tablero[i] = self.turno
            self.botones[i].config(text=self.turno)
            if self.verificar_ganador(self.turno):
                messagebox.showinfo("Fin del juego", f"¡{self.turno} gana!")
                self.resetear()
            elif " " not in self.tablero:
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.resetear()
            else:
                self.turno = self.bot
                self.jugar_maquina()

    def jugar_maquina(self):
        mejor_jugada = self.mejor_movimiento()
        self.tablero[mejor_jugada] = self.bot
        self.botones[mejor_jugada].config(text=self.bot)
        if self.verificar_ganador(self.bot):
            messagebox.showinfo("Fin del juego", f"¡{self.bot} gana!")
            self.resetear()
        elif " " not in self.tablero:
            messagebox.showinfo("Fin del juego", "¡Es un empate!")
            self.resetear()
        else:
            self.turno = "X"

    def mejor_movimiento(self):
        for i in range(9):
            if self.tablero[i] == " ":
                self.tablero[i] = self.bot
                if self.verificar_ganador(self.bot):
                    return i
                self.tablero[i] = " "
        for i in range(9):
            if self.tablero[i] == " ":
                self.tablero[i] = "X"
                if self.verificar_ganador("X"):
                    self.tablero[i] = " "
                    return i
                self.tablero[i] = " "
        return self.tablero.index(" ")  

    def verificar_ganador(self, jugador):
        combinaciones_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                    (0, 4, 8), (2, 4, 6)]
        return any(all(self.tablero[i] == jugador for i in combinacion) for combinacion in combinaciones_ganadoras)

    def resetear(self):
        self.tablero = [" " for _ in range(9)]
        for boton in self.botones:
            boton.config(text=" ")
        self.turno = "X"

if __name__ == "__main__":
    root = tk.Tk()
    juego = TicTacToe(root)
    root.mainloop()