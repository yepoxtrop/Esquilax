'''
========================================================================================================================
FECHA CREACION: 2026/02/23
AUTOR         : LUIS ANGEL SARMIENTO DIAZ
DETALLE       : Clase de label para titulos o textos en la interfaz
MODULOS       : tkinter, ttk
ENTRADAS      : *parent(estructura base), 
                *text(texto), 
                *tamano(tamaño del texto), 
                *negrita(requiere negrita o no)
FECHA MODIFICACION: 2026/02/23
AUTOR MODIFICACION: LUIS ANGEL SARMIENTO DIAZ
MODIFICACION      : Ninguna
========================================================================================================================
'''
import tkinter as tk;
from tkinter import ttk;

class Label(ttk.Label):
    def __init__(
        self, 
        parent:tk.Widget|ttk.Widget, 
        texto:str, 
        tamano:int=16, 
        negrita:bool=True, 
        fuente:str='Arial'
    ):
        super().__init__(master=parent, text=texto);
        self.texto = texto;
        self.tamano = tamano;
        self.negrita = negrita;
        self.fuente = fuente;
        
        '''
        * Configuracion del estilo del label
        '''
        self.configurar_estilo();
    
    '''
    * Configuracion del estilo de tipografia del label
    '''
    def configurar_estilo(self)->None:
        estiloTipografia = [self.fuente, self.tamano];
        if self.negrita:
            estiloTipografia.append('bold');
            tuple(estiloTipografia);
        self.configure(
            font=estiloTipografia,
        ); 