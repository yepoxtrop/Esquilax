'''
========================================================================================================================
FECHA CREACION: 2026/02/23
AUTOR         : LUIS ANGEL SARMIENTO DIAZ
DETALLE       : Clase de frame para los diferentes componentes de la interfaz
MODULOS       : tkinter, ttk
ENTRADAS      : *parent(estructura base), 
                *columnas(numero de columnas del frame), 
                *filas(numero de filas del frame)
FECHA MODIFICACION: 2026/02/23
AUTOR MODIFICACION: LUIS ANGEL SARMIENTO DIAZ
MODIFICACION      : Ninguna
========================================================================================================================
'''
import tkinter as tk;
from tkinter import ttk;

class Frame(ttk.Frame):
    def __init__(self, parent:tk.Widget|ttk.Widget, columnas:int|list=0, filas:int|list=0):
        super().__init__(parent);
        self.columnas = columnas;
        self.filas = filas;
        
        '''
         * Configuracion del grid del frame
         '''
        self.configurar_grid(); 
    
    '''
    * Configuracion del grid del frame
    '''
    def configurar_grid(self):
        if isinstance(self.columnas, int):
            for i in range(self.columnas):
                self.columnconfigure(i, weight=1);
        elif isinstance(self.columnas, list):
            for i in self.columnas:
                posicion = 0;
                self.columnconfigure(posicion, weight=i);
                posicion += 1;
        else:
            raise ValueError('El parametro columnas debe ser un entero o una lista de enteros');
        
        if isinstance(self.filas, int):
            for j in range(self.filas):
                self.rowconfigure(j, weight=1);
        elif isinstance(self.filas, list):
            for j in self.filas:
                posicion = 0;
                self.rowconfigure(posicion, weight=j);
                posicion += 1;
        else:
            raise ValueError('El parametro filas debe ser un entero o una lista de enteros');