'''
========================================================================================================================
FECHA CREACION: 2026/02/23
AUTOR         : LUIS ANGEL SARMIENTO DIAZ
DETALLE       : Modulo de ventana principal de la aplicación, se encarga de configurar la ventana principal y 
                de contener los componentes principales de la aplicación
MODULOS       : tkinter, ttk
COMPONENTES   : Title, Frame, Entry, Button    
FECHA MODIFICACION: 2026/02/23
AUTOR MODIFICACION: LUIS ANGEL SARMIENTO DIAZ
MODIFICACION      : Ninguna
========================================================================================================================
'''
import tkinter as tk;
from tkinter import ttk;

# Componentes
from src.ui.components.label.label import Label;
from src.ui.components.frame.frame import Frame;
from src.ui.components.entry.entry import Entry;
from src.ui.components.button.button import Button;

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__();
        self.configurar_ventana();
        
        '''
        * Titulo de la aplicacion: Frame1 y Titulo1
        * Frame1: Frame para contener el titulo de la aplicacion
        * Titulo1: Label para el titulo de la aplicacion
        '''     
        self.frame1 = Frame(
            parent=self,
            columnas=1,
            filas=1
        );
        self.titulo1 = Label(
            parent=self.frame1,
            texto='Esquilax',
            tamano=20,
            negrita=False,
            fuente='Arial'
        );
        self.frame1.grid(row=0, column=0, padx=10, pady=5, sticky='nsew');
        self.titulo1.grid(row=0, column=0,  padx=10, pady=5);
       
        '''
        * Campo de texto: Frame2, Label2, Entry1, Button1
        * Frame2: Frame para contener el campo de texto y el boton de busqueda
        * Label2: Label para el texto del campo de texto
        * Entry1: Entry para el campo de texto
        * Button1: Button para el boton de busqueda
        '''
        self.frame2 = Frame(
            parent=self,
            columnas=2,
            filas=2
        );
        self.titulo2 = Label(
            parent=self.frame2,
            texto='Ingresa la URL del video que deseas descargar:',
            negrita=False,
            fuente='Arial',
            tamano=13
        );
        self.entry1 = Entry(
            parent=self.frame2,
            tamano=12
        );
        self.button1 = Button(
            parent=self.frame2,
            text='Buscar'
        )
        self.frame2.grid(row=1, column=0, sticky='nsew');
        self.titulo2.grid(row=0, column=0, padx=10, pady=5, sticky='w', columnspan=2);
        self.entry1.grid(row=1, column=0, padx=10, pady=5, sticky='ew');
        self.button1.grid(row=1, column=1, pady=5, padx=10, sticky='ew');
        
        '''
        * Datos del video: Frame3, Table1
        '''
        self.frame3 = Frame(
            parent=self,
            columnas=1,
            filas=1
        );
        self.frame3.grid(row=2, column=0, sticky='nsew');
        # Incompleto
        
        '''
        * Boton de descarga: Frame4, Button2
        '''
        self.frame4 = Frame(
            parent=self,
            columnas=1,
            filas=1
        );
        self.button2 = Button(
            parent=self.frame4,
            text='Descargar Video'
        );
        self.frame4.grid(row=3, column=0, sticky='nsew');
        self.button2.grid(row=0, column=0, padx=10, pady=5,); 
        
        '''
        * Barra de estado
        '''
        # Incompleto
        
        '''
        * Creditos: 
        '''
        
    def configurar_ventana(self):
        # Configuraciones basicas 
        self.geometry('600x500');
        self.resizable(0,0);
        self.title('ESQUILAX');
        self.iconbitmap('src/ui/assets/icons/logo.ico');
        
        # Configuracion del flex
        self.columnconfigure(0, weight=1);
        self.rowconfigure(0, weight=0);
        self.rowconfigure(1, weight=0);
        self.rowconfigure(2, weight=0);
        self.rowconfigure(3, weight=0);
        self.rowconfigure(4, weight=0);
        self.rowconfigure(5, weight=0);
        
    def configurar_estilos(self):
        estilos = ttk.Style();
        estilos.theme_use('clam');
        estilos.configure('TFrame', background='#f0f0f0');