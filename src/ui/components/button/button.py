# Modulos
import tkinter as tk;
from tkinter import ttk;

class Button(ttk.Button):
    def __init__(self, parent, text):
        super().__init__(parent, text=text);