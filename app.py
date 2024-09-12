import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import sys
import os

from idlelib.colorizer import ColorDelegator
from idlelib.percolator import Percolator

# Configuraciones de la ventana principal
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema azul

class PythonIDE(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Python IDE")
        self.geometry("900x600")

        # Establecer el ícono
        self.set_icon("iconpy.png")  # Usa un archivo .png o .gif

        # Editor de código con números de línea
        self.create_editor()

        # Consola de salida
        self.create_console()

        # Botones
        self.create_buttons()

    def set_icon(self, icon_path):
        # Usar Pillow para establecer el ícono
        try:
            img = Image.open(icon_path)
            photo = ImageTk.PhotoImage(img)
            self.iconphoto(True, photo)
        except Exception as e:
            print(f"Error: Unable to set the icon. Check if '{icon_path}' is a valid image file.")
            print(e)

    def create_editor(self):
        # Frame para el editor de código
        self.editor_frame = ctk.CTkFrame(self)
        self.editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Scrollbar
        self.scrollbar = ctk.CTkScrollbar(self.editor_frame, orientation='vertical')
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text widget para el editor de código
        self.editor = tk.Text(self.editor_frame, wrap=tk.NONE, undo=True, font=("Consolas", 12))
        self.editor.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.editor.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.editor.yview)

        # Resaltado de sintaxis
        self.add_syntax_highlighting()

    def add_syntax_highlighting(self):
        # Uso de ColorDelegator de idlelib para resaltado de sintaxis
        delegator = ColorDelegator()
        Percolator(self.editor).insertfilter(delegator)

    def create_console(self):
        # Consola de salida
        self.console_frame = ctk.CTkFrame(self)
        self.console_frame.pack(fill=tk.BOTH, padx=10, pady=5)
        self.console = tk.Text(self.console_frame, height=10, state=tk.DISABLED, bg="#1e1e1e", fg="white", font=("Consolas", 12))
        self.console.pack(fill=tk.BOTH, expand=True)

    def create_buttons(self):
        # Botones para ejecutar y abrir archivos
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill=tk.X, pady=10)

        self.run_button = ctk.CTkButton(button_frame, text="Run", command=self.run_code)
        self.run_button.pack(side=tk.LEFT, padx=5)

        self.open_button = ctk.CTkButton(button_frame, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=5)

    def run_code(self):
        code = self.editor.get("1.0", tk.END)
        self.console.config(state=tk.NORMAL)
        self.console.delete("1.0", tk.END)

        # Guardar el código en un archivo temporal
        with open("temp_script.py", "w") as f:
            f.write(code)

        # Ejecutar el código y mostrar la salida en la consola
        try:
            output = subprocess.check_output([sys.executable, "temp_script.py"], stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output = e.output

        self.console.insert(tk.END, output)
        self.console.config(state=tk.DISABLED)

    def open_file(self):
        # Función para abrir archivos Python
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
            self.editor.delete("1.0", tk.END)
            self.editor.insert("1.0", code)

if __name__ == "__main__":
    app = PythonIDE()
    app.mainloop()
