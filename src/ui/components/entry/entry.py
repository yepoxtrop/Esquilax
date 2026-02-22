# Modulos
import tkinter as tk;
from tkinter import ttk;

class Entry(ttk.Entry):
    
    def __init__(self, parent, font):
        super().__init__(parent);
        self.configurar_estilo(font);
        
    def configurar_estilo(self, font):
        self.configure(
            font=font,
        );