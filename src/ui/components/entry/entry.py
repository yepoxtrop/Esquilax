'''
========================================================================================================================
FECHA CREACION: 2026/02/23
AUTOR         : LUIS ANGEL SARMIENTO DIAZ
DETALLE       : Modulo de entrada de texto para la aplicación, se encarga de configurar el campo de texto 
                para la busqueda del video a descargar
MODULOS       : tkinter, ttk
ENTRADAS      : *parent(estructura base), 
                *fuente(tipo de letra del texto), 
                *tamano(tamaño del texto)
FECHA MODIFICACION: 2026/02/23
AUTOR MODIFICACION: LUIS ANGEL SARMIENTO DIAZ
MODIFICACION      : Ninguna
========================================================================================================================
'''
import tkinter as tk;
from tkinter import ttk;

class Entry(ttk.Entry):
    
    def __init__(self, parent, fuente:str='Arial', tamano:int=13):
        super().__init__(parent);
        self.fuente = fuente;
        self.tamano = tamano;
        self.configurar_estilo();
        
    def configurar_estilo(self):
        font = (self.fuente, self.tamano);
        self.configure(
            font=font,
        );