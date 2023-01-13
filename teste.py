import tkinter as tk
from tkinter import *
import os
from PIL import Image,ImageTk
import time


class overlay():       
    def pergunta(self):
        global n 
        n = 'nao'
        while n != 's': 
            n = input('deseja fechar a aplicação?')
            if n == 's':       
                root.destroy()   
                
    def abrir(self,func=pergunta,position='.'):
        global root
        root = tk.Tk()
        root.overrideredirect(True) 
        root.attributes("-alpha", 0.5)# faz a janela ficar transparente
        root.attributes("-topmost", True)# faz ficar em cima de qualquer outro processo
        largura = root.winfo_screenwidth()*0.15
        altura = root.winfo_screenheight()*0.15
        root.geometry('{}x{}+{}+0'.format(int(largura), int(altura), int(root.winfo_screenwidth()-largura)))         
        match position:
            case 'top-left':
                root.geometry('{}x{}+0+0'.format(int(largura), int(altura)))     
            case 'bottom-right':
                root.geometry('{}x{}+{}+{}'.format(int(largura), int(altura), int(root.winfo_screenwidth()-largura), int(root.winfo_screenheight()-altura)))
            case 'bottom-left':
                root.geometry('{}x{}+0+{}'.format(int(largura), int(altura), int(root.winfo_screenheight()-altura)))
        
        # root.geometry("200x200+0+{}". format(root.winfo_screenheight()- 500))# tamanho da janela + a posição         
        label_img= Label(root,width= int(largura*0.050), height= int(altura*0.050), anchor= CENTER)
        label_img.pack() 
       
       
        root.after(0, func(self))
        root.mainloop()

def pergunta2(self):
        global n 
        n = 'nao'
        while n != 's': 
            n = input('deseja fechar a aplicação?')
            if n == 's':       
                root.destroy()   


# incializar a aplicação

overlay = overlay()

overlay.abrir()