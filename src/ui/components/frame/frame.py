# Modulos
import tkinter as tk;
from tkinter import ttk;

class Frame(ttk.Frame):
    def __init__(self, parent, columnas, filas):
        super().__init__(parent);
        self.columnas = columnas;
        self.filas = filas;
        self.configurar_grid(); 
        
    def configurar_grid(self):
        for i in range(self.columnas):
            self.columnconfigure(i, weight=1);
        for j in range(self.filas):
            self.rowconfigure(j, weight=1);