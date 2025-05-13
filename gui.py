import tkinter as tk
from tkinter import filedialog, messagebox
import os
import time

import entrenador
import comparador

hash_db = {"algoritmo": None}

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reconocimiento de Canciones")
        self.algoritmo = tk.StringVar()
        self.crear_menu_principal()

    def crear_menu_principal(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Menú Principal", font=("Helvetica", 16, "bold")).pack(pady=10)

        tk.Button(self.root, text="Entrenar", command=self.menu_entrenamiento, width=30).pack(pady=5)
        tk.Button(self.root, text="Comparar", command=self.menu_comparacion, width=30).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.quit, width=30).pack(pady=5)

    def seleccionar_algoritmo(self, callback):
        self.limpiar_ventana()
        tk.Label(self.root, text="Selecciona un algoritmo de hash", font=("Helvetica", 14)).pack(pady=10)

        for alg in ["MD5", "SHA-1", "SHA-256"]:
            tk.Radiobutton(self.root, text=alg, variable=self.algoritmo, value=alg).pack(anchor="w", padx=20)

        tk.Button(self.root, text="Aceptar", command=callback).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.crear_menu_principal).pack()

    def menu_entrenamiento(self):
        self.seleccionar_algoritmo(self.mostrar_opciones_entrenamiento)

    def menu_comparacion(self):
        self.seleccionar_algoritmo(self.mostrar_opciones_comparacion)

    def mostrar_opciones_entrenamiento(self):
        algoritmo = self.algoritmo.get()
        if not algoritmo:
            messagebox.showerror("Error", "Debes seleccionar un algoritmo.")
            return

        if hash_db["algoritmo"] != algoritmo:
            hash_db["algoritmo"] = algoritmo

        self.limpiar_ventana()
        tk.Label(self.root, text="Modo de Entrenamiento", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.root, text="Entrenar un directorio", command=self.entrenar_directorio).pack(pady=5)
        tk.Button(self.root, text="Entrenar una canción", command=self.entrenar_cancion).pack(pady=5)
        tk.Button(self.root, text="Entrenar directorio de pruebas", command=self.entrenar_directorio_pruebas).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.crear_menu_principal).pack(pady=10)

    def mostrar_opciones_comparacion(self):
        algoritmo = self.algoritmo.get()
        if not algoritmo:
            messagebox.showerror("Error", "Debes seleccionar un algoritmo.")
            return

        self.limpiar_ventana()
        tk.Label(self.root, text="Modo de Comparación", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.root, text="Comparar archivo MP3", command=self.comparar_archivo).pack(pady=5)
        tk.Button(self.root, text="Comparar usando grabadora", command=lambda: self.llamar_comparador_grabadora(algoritmo)).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.crear_menu_principal).pack(pady=10)

    def entrenar_directorio(self):
        path = filedialog.askdirectory()
        if path:
            # Aquí debes llamar a tu función de entrenamiento en directorio
            messagebox.showinfo("Entrenamiento", f"Entrenamiento en {path} iniciado... (simulado)")

    def entrenar_cancion(self):
        path = filedialog.askopenfilename(filetypes=[("Archivos MP3", "*.mp3")])
        if path:
            tiempo0 = time.time()
            entrenador.entrenar_archivo(path, self.algoritmo.get())
            tiempo1 = time.time()
            messagebox.showinfo("Éxito", f"Entrenamiento completado en {tiempo1 - tiempo0:.2f} segundos.")

    def entrenar_directorio_pruebas(self):
        tiempo0 = time.time()
        entrenador.entrenar_directorio_pruebas(self.algoritmo.get())
        tiempo1 = time.time()
        messagebox.showinfo("Éxito", f"Entrenamiento en pruebas completado en {tiempo1 - tiempo0:.2f} segundos.")

    def comparar_archivo(self):
        path = filedialog.askopenfilename(filetypes=[("Archivos MP3", "*.mp3")])
        if not path:
            return
        if not path.lower().endswith(".mp3"):
            messagebox.showerror("Error", "El archivo seleccionado no es MP3.")
            return
        comparador.comparador(path, self.algoritmo.get())

    def llamar_comparador_grabadora(self, algoritmo):
        comparador.comparador_al_menos_una_coincidencia(algoritmo)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
