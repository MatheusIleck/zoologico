import sys
sys.path.append('./db_zoo/')

import database
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

class subnivel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.protocol("WM_DELETE_WINDOW", self.fechar_janela_admin)
        self.geometry("1920x1080")
        self.configure(fg_color='#FFFFFF')
        self.title('Zoologico')
    
    def fechar_janela_admin(self):
        self.master.deiconify()  # Exibe a janela de login
        self.destroy()  # Destroi a janela do administrador

class App(ctk.CTk):
    def __init__(self):
        super().__init__() 
        #configuração da tela de login
        self.geometry('500x500')
        self.title('Zoologico')
        self.resizable(False,False)
        self.configure(fg_color='#3BA37E')
        self.fonte = ctk.CTkFont(family='Poppins', size=40, weight='bold', underline=False)

        #conteudo login
        self.logoctk = ctk.CTkImage(light_image=Image.open('./imagens/teste.png'), size=(110,110))
        self.logo = ctk.CTkLabel(master=self, image=self.logoctk,text=None)
        self.logo.pack(padx=0, pady=(20))

        self.texto_bemvindo = ctk.CTkLabel(self, text='ZOOLOGICO', text_color='#fff', font=self.fonte)
        self.texto_bemvindo.pack(padx=0, pady=0)

        self.texto_bemvindo2 = ctk.CTkLabel(self, text='SEJA BEM VINDO!', text_color='#fff', font=('Poppins', 15, 'bold'))
        self.texto_bemvindo2.pack(padx=0, pady=0)

        self.login = ctk.CTkEntry(self, placeholder_text='Digite o CPF', width=200, corner_radius=20, font=('Poppins',15))
        self.login.pack()

        self.senha = ctk.CTkEntry(self, placeholder_text='Digite a senha', width=200, corner_radius=20, font=('Poppins', 15))
        self.senha.pack()

        self.botao_login = ctk.CTkButton(self, text='Login', command=self.logando)
        self.botao_login.pack()

    def janela_administrador(self):
        janela_admin = subnivel(self)

        # Componentes da barra de menu
        barra_menu = ctk.CTkFrame(master=janela_admin, height=900, corner_radius=0, bg_color='#9FB79F')
        barra_menu.grid(row=0, column=0, columnspan=4, sticky='ew')

        
        icone_funcionario = ctk.CTkImage(light_image=Image.open('./imagens/icone_funcionario.png'), size=(40, 40))
        botao_funcionario = ctk.CTkButton(barra_menu, image=icone_funcionario, text='Funcionário', compound='left', corner_radius=0, width=480, height=100, fg_color='#9FB79F', text_color='#0B724C', font=('Poppins', 20, 'bold'), hover_color='#9FB79F')
        botao_funcionario.grid(row=0, column=0)

        icone_ambiente = ctk.CTkImage(light_image=Image.open('./imagens/teste.png'))
        botao_ambiente = ctk.CTkButton(barra_menu, image=icone_ambiente, text='Ambiente', compound='left', corner_radius=0, width=480, height=100, fg_color='#9FB79F', text_color='#0B724C', font=('Poppins', 20, 'bold'), hover_color='#9FB79F')
        botao_ambiente.grid(row=0, column=1)

        icone_estoque = ctk.CTkImage(light_image=Image.open('./imagens/teste.png'))
        botao_estoque = ctk.CTkButton(barra_menu, image=icone_estoque, text='Estoque', compound='left', corner_radius=0, width=480, height=100, fg_color='#9FB79F', text_color='#0B724C', font=('Poppins', 20, 'bold'), hover_color='#9FB79F')
        botao_estoque.grid(row=0, column=2)
        
        icone_sair = ctk.CTkImage(light_image=Image.open('./imagens/teste.png'))
        botao_sair = ctk.CTkButton(barra_menu, image=icone_sair, text='Sair', compound='left', corner_radius=0, width=480, height=100, fg_color='#9FB79F', text_color='#0B724C', font=('Poppins', 20, 'bold'), hover_color='#9FB79F')
        botao_sair.grid(row=0, column=3)

        barra_tela_principal = ctk.CTkFrame(master=janela_admin, height=900, corner_radius=0)
        barra_tela_principal.grid(row=1, column=0, columnspan=4, sticky='ew')
        
        esquerda_barra_menu = ctk.CTkFrame(master=barra_tela_principal,corner_radius=0, height=900)
        esquerda_barra_menu.grid(row=1,column=0)

        #componentes da janela administrador
        foto_funcionario = ctk.CTkImage(light_image=Image.open('./imagens/eu.png'), size=(280, 280))
        base_foto = ctk.CTkLabel(esquerda_barra_menu, height= 200, width=640, image=foto_funcionario, text=None, bg_color='#fff')
        base_foto.grid(row=0, column=0, padx=0, pady=0, columnspan=2)
    
        '''

        
        texto = ctk.CTkLabel(barra_tela_principal, text='DALE', bg_color='blue', font=('Arial', 12))
        texto.grid(row=1, column=1, padx=10, pady=10)

        texto2 = ctk.CTkLabel(barra_tela_principal, text='dele', bg_color='blue', font=('Arial', 12))
        texto2.grid(row=2, column=2, padx=10, pady=10)'''   


    def logando(self):
        login = self.login.get()
        senha = self.senha.get()
        if login and senha:
            # Verifica as credenciais no banco de dados
            database.cursor.execute("SELECT * FROM users WHERE (Cpf=? and Senha=?)", (login, senha))
            result = database.cursor.fetchone()
            if result:
                messagebox.showinfo('Login', 'Bem vindo!')
                self.withdraw()
                self.janela_administrador()  # Abre a janela de administrador
            else:
                messagebox.showinfo('Falha', 'Credenciais inválidas')


zoologico = App()
zoologico.mainloop()


