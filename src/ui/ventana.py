# Modulos
import tkinter as tk;
from tkinter import ttk;

# Componentes
from src.ui.components.title.title import Title;
from src.ui.components.frame.frame import Frame;
from src.ui.components.entry.entry import Entry;
from src.ui.components.button.button import Button;

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__();
        self.configurar_ventana();
        self.title = Title(self, text='Descarga los Videos que Quieras 😈');
        self.title.grid(row=0, column=0);
        
        # Primer Frame
        self.frame1 = Frame(self, columnas=1, filas=2); 
        self.frame1.grid(row=1, column=0, sticky=tk.EW);
        self.subtitulo1 = Title(self.frame1, text='Ingresa el enlace del video que deseas descargar:', tamano=12, negrita=False);
        self.subtitulo1.grid(row=0, column=0, sticky=tk.EW);
        self.entrada1 = Entry(self.frame1, font=('Arial', 12));
        self.entrada1.grid(row=1, column=0, sticky=tk.EW);
        
        # Segundo Frame
        self.frame2 = Frame(self, columnas=1, filas=1);
        self.frame2.grid(row=2, column=0, sticky=tk.EW);
        self.button1 = Button(self.frame2, text='Pegar enlace');
        self.button1.grid(row=0, column=0, sticky=tk.EW);
        
        # Tercer Frame
        
        # Cuarto Frame
        self.frame4 = Frame(self, columnas=1, filas=1);
        self.frame4.grid(row=3, column=0, sticky=tk.EW);
        self.button3 = Button(self.frame4, text='Descargrar Video');
        self.button3.grid(row=0, column=0, sticky=tk.EW);
        
        
        
    def configurar_ventana(self):
        # Configuraciones basicas 
        self.geometry('600x500');
        self.resizable(0,0);
        self.title('Esquilax');
        self.iconbitmap('src/ui/assets/icons/logo.ico');
        
        # Configuracion del flex
        self.columnconfigure(0, weight=1);
        self.rowconfigure(0, weight=0);
        self.rowconfigure(1, weight=1);
        self.rowconfigure(2, weight=1);
        self.rowconfigure(3, weight=1);
        self.rowconfigure(4, weight=1);
        self.rowconfigure(5, weight=1);
        
    def configurar_estilos(self):
        estilos = ttk.Style();
        estilos.configure('TFrame', background='#f0f0f0');