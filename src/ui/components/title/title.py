# Modulos
import tkinter as tk;
from tkinter import ttk;

class Title(ttk.Label):
    def __init__(self, parent, text, tamano=16, negrita=True):
        super().__init__(parent, text=text);
        self.configurar_estilo(tamano, negrita);
    
    def configurar_estilo(self, tamano, negrita):
        estilo = 'bold' if negrita else 'normal';
        self.configure(
            font=('Arial', tamano, estilo),
        );