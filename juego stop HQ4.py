import tkinter as tk
from tkinter import messagebox, ttk
import random
import time


CATEGORIAS = [
    "Nombre",
    "Ciudad/País",
    "Animal",
    "Fruta/Comida",
    "Objeto",
    "Profesión",
]

LETRAS = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")  

AJUSTES_DIFICULTAD = {
    "Fácil": {"time": 60, "ai_blank_chance": 0.25, "ai_common_bias": 0.8},
    "Normal": {"time": 45, "ai_blank_chance": 0.15, "ai_common_bias": 0.5},
    "are you crazy? HARD": {"time": 30, "ai_blank_chance": 0.05, "ai_common_bias": 0.2},
}


PISCINAS_PALABRAS = {
    "Nombre": [
        "Ana", "Antonio", "Beatriz", "Carlos", "Carmen", "Daniel", "Diego", "Elena", "Esteban",
        "Francisco", "Fernando", "Gabriela", "Gonzalo", "Héctor", "Inés", "Iván", "Javier",
        "Juana", "Karla", "Laura", "Luis", "María", "Miguel", "Natalia", "Nicolás", "Óscar",
        "Patricia", "Pablo", "Queralt", "Ricardo", "Raquel", "Sara", "Sergio", "Tomás", "Unai",
        "Víctor", "Ximena", "Yolanda", "Zacarías",
    ],
    "Ciudad/País": [
        "Argentina", "Barcelona", "Brasil", "Canarias", "Chile", "Colombia", "Durango",
        "Ecuador", "España", "Francia", "Granada", "Honduras", "India", "Japón", "Kenia",
        "Lima", "Lisboa", "México", "Murcia", "Nicaragua", "Noruega", "Oslo", "París",
        "Perú", "Quito", "Roma", "Rusia", "Sevilla", "Suiza", "Tokio", "Tenerife",
        "Uganda", "Valencia", "Venezuela", "Zaragoza",
    ],
    "Animal": [
        "Águila", "Antílope", "Ballena", "Burro", "Caballo", "Cebra", "Delfín", "Dragón (mit.)",
        "Elefante", "Erizo", "Foca", "Faisán", "Gato", "Gorila", "Hipopótamo", "Iguana",
        "Jirafa", "Jaguar", "Koala", "Lobo", "León", "Mono", "Murciélago", "Nutria",
        "Oso", "Oveja", "Pato", "Perro", "Quetzal", "Rinoceronte", "Rana", "Serpiente",
        "Tigre", "Tortuga", "Urraca", "Vaca", "Zorro",
    ],
    "Fruta/Comida": [
        "Albaricoque", "Arroz", "Banana", "Berenjena", "Cereza", "Chocolate", "Dátil",
        "Durazno", "Ensalada", "Fresa", "Frambuesa", "Guisantes", "Galleta", "Huevo",
        "Helado", "Kiwi", "Ketchup", "Lima", "Limón", "Mango", "Manzana", "Naranja",
        "Nuez", "Oliva", "Pasta", "Pan", "Queso", "Quinoa", "Rábano", "Sopa", "Tomate",
        "Turrón", "Uva", "Vainilla", "Zanahoria",
    ],
    "Objeto": [
        "Agenda", "Avión", "Bolígrafo", "Bicicleta", "Cámara", "Computadora", "Daga",
        "Dado", "Espejo", "Escoba", "Foco", "Flauta", "Guitarra", "Gafas", "Herramienta",
        "Illa (bot.)", "Impresora", "Jarrón", "Juguete", "Llave", "Libro", "Mesa",
        "Micrófono", "Navaja", "Ordenador", "Paraguas", "Ratón", "Reloj", "Teléfono",
        "Televisor", "Vela", "Ventana", "Xilófono", "Yunque", "Zapato",
    ],
    "Profesión": [
        "Abogado", "Actor", "Arquitecto", "Bombero", "Biólogo", "Carpintero", "Cocinero",
        "Dentista", "Doctor", "Diseñador", "Economista", "Enfermero", "Farmacéutico",
        "Fotógrafo", "Ingeniero", "Juez", "Joyero", "Kinesiólogo", "Maestro", "Mecánico",
        "Niñera", "Nutricionista", "Odontólogo", "Pintor", "Periodista", "Psicólogo",
        "Químico", "Profesor", "Piloto", "Sastre", "Taxista", "Veterinario",
    ],
}


def ia_generar_respuesta(categoria, letra, nombre_dificultad):
    ajustes = AJUSTES_DIFICULTAD[nombre_dificultad]
    
    if random.random() < ajustes["ai_blank_chance"]:
        return ""
    pool = PISCINAS_PALABRAS.get(categoria, [])
   
    def empieza_por(palabra, letra):
        if not palabra:
            return False
        w = palabra.upper()
        first = w[0]
        return first == letra.upper()
    candidatos = [w for w in pool if empieza_por(w, letra)]
    if not candidatos:
        normalizadas = []
        for w in pool:
            wf = w.upper()
            wf = wf.replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
            if wf and wf[0] == letra.upper():
                normalizadas.append(w)
        candidatos = normalizadas
    if not candidatos:
        
        return (letra.upper() + "..." )
    
    bias = ajustes["ai_common_bias"]
    scored = []
    for w in candidatos:
        score = len(w)  
        scored.append((w, score))
    scored_ordenado = sorted(scored, key=lambda x: x[1])
    if random.random() < bias:
        cutoff = max(1, int(len(scored_ordenado) * 0.4))
        eleccion = random.choice(scored_ordenado[:cutoff])[0]
    else:
        cutoff = max(1, int(len(scored_ordenado) * 0.4))
        eleccion = random.choice(scored_ordenado[-cutoff:])[0]
    return eleccion

class JuegoStopApp:
    def __init__(self, raiz):
        self.raiz = raiz
        raiz.title("STOP! - Máquina vs Humano")
        self.letra = tk.StringVar(value="?")
        self.dificultad = tk.StringVar(value="Normal")
        self.tiempo_restante = tk.IntVar(value=0)
        self.entradas = {}
        self.respuestas_ia = {}
        self.respuestas_humano = {}
        self.ejecutando = False
        self.dificultad_seleccionada = "Normal"
        self.crear_widgets()

    def crear_widgets(self):
        top = ttk.Frame(self.raiz, padding=10)
        top.grid(row=0, column=0, sticky="nsew")

        
        lbl_diff = ttk.Label(top, text="Dificultad:")
        lbl_diff.grid(row=0, column=0, sticky="w")
        self.combo_dificultad = ttk.Combobox(top, values=list(AJUSTES_DIFICULTAD.keys()), state="readonly")
        self.combo_dificultad.set("Normal")
        self.combo_dificultad.grid(row=0, column=1, sticky="w")
        self.combo_dificultad.bind("<<ComboboxSelected>>", self.al_cambio_dificultad)

        
        self.btn_iniciar = ttk.Button(top, text="Iniciar ronda", command=self.iniciar_ronda)
        self.btn_iniciar.grid(row=0, column=2, padx=5)
        self.btn_parar = ttk.Button(top, text="Parar (submit)", command=self.parar_ronda, state="disabled")
        self.btn_parar.grid(row=0, column=3, padx=5)

        
        frame_letra = ttk.Frame(self.raiz, padding=10, relief="ridge")
        frame_letra.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        ttk.Label(frame_letra, text="Letra:").grid(row=0, column=0, sticky="w")
        self.lbl_letra = ttk.Label(frame_letra, textvariable=self.letra, font=("Helvetica", 32))
        self.lbl_letra.grid(row=0, column=1, padx=10)
        ttk.Label(frame_letra, text="Tiempo:").grid(row=0, column=2, sticky="w", padx=(20,0))
        self.lbl_tiempo = ttk.Label(frame_letra, textvariable=self.tiempo_restante, font=("Helvetica", 18))
        self.lbl_tiempo.grid(row=0, column=3, padx=5)

      
        frame_entradas = ttk.Frame(self.raiz, padding=10)
        frame_entradas.grid(row=2, column=0, sticky="nsew")
        self.vars_entrada = {}
        for i, cat in enumerate(CATEGORIAS):
            ttk.Label(frame_entradas, text=f"{cat}:").grid(row=i, column=0, sticky="e", pady=2)
            var = tk.StringVar()
            ent = ttk.Entry(frame_entradas, textvariable=var, width=40, state="disabled")
            ent.grid(row=i, column=1, sticky="w", pady=2)
            self.vars_entrada[cat] = var
            self.entradas[cat] = ent

        0
        frame_resultados = ttk.Frame(self.raiz, padding=10, relief="groove")
        frame_resultados.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
        self.texto_resultados = tk.Text(frame_resultados, height=12, state="disabled", wrap="word")
        self.texto_resultados.pack(fill="both", expand=True)

    def al_cambio_dificultad(self, _evento):
        val = self.combo_dificultad.get()
        self.dificultad_seleccionada = val

    def iniciar_ronda(self):
        if self.ejecutando:
            return
        
        for var in self.vars_entrada.values():
            var.set("")
        self.texto_resultados.configure(state="normal")
        self.texto_resultados.delete("1.0", tk.END)
        self.texto_resultados.configure(state="disabled")
        
        self.eleccion_letra = random.choice(LETRAS)
        self.letra.set(self.eleccion_letra)
        
        ajustes = AJUSTES_DIFICULTAD.get(self.dificultad_seleccionada, AJUSTES_DIFICULTAD["Normal"])
        self.tiempo_restante.set(ajustes["time"])
        
        for ent in self.entradas.values():
            ent.configure(state="normal")
        self.btn_iniciar.configure(state="disabled")
        self.btn_parar.configure(state="normal")
        self.ejecutando = True
        self.cuenta_regresiva()

    def cuenta_regresiva(self):
        if not self.ejecutando:
            return
        t = self.tiempo_restante.get()
        if t <= 0:
            self.parar_ronda()
            return
        self.tiempo_restante.set(t - 1)
        self.raiz.after(1000, self.cuenta_regresiva)

    def parar_ronda(self):
        if not self.ejecutando:
            return
        self.ejecutando = False
       
        for ent in self.entradas.values():
            ent.configure(state="disabled")
        self.btn_iniciar.configure(state="normal")
        self.btn_parar.configure(state="disabled")
       
        humano = {}
        for cat, var in self.vars_entrada.items():
            texto = var.get().strip()
            humano[cat] = texto
        self.respuestas_humano = humano
        
        ia = {}
        for cat in CATEGORIAS:
            ans = ia_generar_respuesta(cat, self.eleccion_letra, self.dificultad_seleccionada)
            ia[cat] = ans
        self.respuestas_ia = ia
        
        puntuacion_humano = 0
        puntuacion_ia = 0
        detalles = []
        for cat in CATEGORIAS:
            h = humano.get(cat, "").strip()
            a = ia.get(cat, "").strip()
            
            valido_h = False
            if h:
                hfirst = h[0].upper()
                hfirst = hfirst.replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
                esperado = self.eleccion_letra.upper()
                if hfirst == esperado:
                    valido_h = True
                else:
                    valido_h = False
            
            valido_a = bool(a) and (a[0].upper() == self.eleccion_letra.upper() or a[0].upper() == self.eleccion_letra.upper())
            
            
            
            
            nota_ronda = f"{cat} | Humano: '{h or '-'}' | Máquina: '{a or '-'}' -> "
            if not valido_h and not valido_a:
                nota_ronda += "Ninguno válido (0 pts cada uno)"
            elif valido_h and valido_a:
                if h.lower() == a.lower():
                    puntuacion_humano += 5
                    puntuacion_ia += 5
                    nota_ronda += "Misma respuesta (5 pts cada uno)"
                else:
                    puntuacion_humano += 10
                    puntuacion_ia += 10
                    nota_ronda += "Respuestas distintas (10 pts cada uno)"
            elif valido_h and not valido_a:
                puntuacion_humano += 10
                nota_ronda += "Solo humano válido (Humano +10)"
            elif valido_a and not valido_h:
                puntuacion_ia += 10
                nota_ronda += "Solo máquina válida (Máquina +10)"
            detalles.append(nota_ronda)
        
        self.texto_resultados.configure(state="normal")
        self.texto_resultados.insert(tk.END, f"Letra: {self.eleccion_letra}\n")
        self.texto_resultados.insert(tk.END, f"Dificultad: {self.dificultad_seleccionada}\n")
        self.texto_resultados.insert(tk.END, "-"*50 + "\n")
        for d in detalles:
            self.texto_resultados.insert(tk.END, d + "\n")
        self.texto_resultados.insert(tk.END, "-"*50 + "\n")
        self.texto_resultados.insert(tk.END, f"Puntuación Humano: {puntuacion_humano}\n")
        self.texto_resultados.insert(tk.END, f"Puntuación Máquina: {puntuacion_ia}\n")
        if puntuacion_humano > puntuacion_ia:
            ganador = "Humano gana la ronda!"
        elif puntuacion_humano < puntuacion_ia:
            ganador = "Máquina gana la ronda!"
        else:
            ganador = "Empate!"
        self.texto_resultados.insert(tk.END, f"Resultado: {ganador}\n")
        self.texto_resultados.configure(state="disabled")
        
        messagebox.showinfo("Ronda finalizada", f"Humano: {puntuacion_humano}  Máquina: {puntuacion_ia}\n{ganador}")

def main():
    raiz = tk.Tk()
    style = ttk.Style()
    try:
        style.theme_use('clam')
    except:
        pass
    app = JuegoStopApp(raiz)
    raiz.mainloop()

if __name__ == "__main__":
    main()
