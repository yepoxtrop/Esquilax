# Modulos
import tkinter as tk;
from tkinter import ttk;

class Canva(tk.Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs);