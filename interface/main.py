import sys
sys.path.append('./db_zoo/')

import database
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1920x1080")
        self.configure(fg_color='#3BA37E')
        self.title('Zoologico')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tela_login()
        
    def janela_administrador(self):
        # Oculta a janela de login
        self.withdraw()

        # Cria a janela do administrador
        janela_admin = ToplevelWindow()

        # Componentes da tela de administrador
        botao_funcionario = ctk.CTkButton(janela_admin, text='Funcionário')
        botao_funcionario.grid(row=0, column=0)
        botao_locais = ctk.CTkButton(janela_admin, text='Locais')
        botao_locais.grid(row=0, column=1)
        botao_teste = ctk.CTkButton(janela_admin, text='Teste')
        botao_teste.grid(row=0, column=2)
        botao_sair = ctk.CTkButton(janela_admin, text='Sair', command=self.fechar_janela_admin)
        botao_sair.grid(row=0, column=3)

    def tela_login(self):
        # Cria a janela de login
        janela_login = ctk.CTk()
        janela_login.title('Zoologico - Login')
        janela_login.geometry('500x500')
        janela_login.resizable(False, False)
        janela_login.configure(fg_color='#3BA37E')

        # Função de login
        def logando():
            login = login_entry.get()
            senha = senha_entry.get()
            if login and senha:
                # Verifica as credenciais no banco de dados
                database.cursor.execute("SELECT * FROM users WHERE (Cpf=? and Senha=?)", (login, senha))
                result = database.cursor.fetchone()
                if result:
                    messagebox.showinfo('Login', 'Bem vindo!')
                    self.janela_administrador()  # Abre a janela de administrador
                else:
                    messagebox.showinfo('Falha', 'Credenciais inválidas')

        # Componentes da janela de login
        my_image = ctk.CTkImage(light_image=Image.open("/teste.png"),
                                  dark_image=Image.open("/teste.png"),
                                  size=(30, 30))
        print(my_image)
        fonte = ctk.CTkFont(family='Poppins', size=40, weight='bold', underline=False)
        texto_bemvindo = ctk.CTkLabel(janela_login, text="ZOOLOGICO", text_color='#fff', font=fonte)
        texto_bemvindo.pack(padx=10, pady=0)

        texto_bemvindo = ctk.CTkLabel(janela_login, text="SEJA BEM VINDO!", text_color='#fff', font=('Poppins', 15, 'bold'))
        texto_bemvindo.pack(padx=5, pady=0)

        login_entry = ctk.CTkEntry(janela_login, placeholder_text='Digite o CPF', width=200, corner_radius=20, font=('Poppins', 15))
        login_entry.pack(padx=10, pady=10)

        senha_entry = ctk.CTkEntry(janela_login, placeholder_text='Digite a senha', width=200, corner_radius=20, font=('Poppins', 15))
        senha_entry.pack()

        login_button = ctk.CTkButton(janela_login, text='Login', command=logando)
        login_button.pack(padx=10, pady=10)

        janela_login.mainloop()

    def fechar_janela_admin(self):
        # Fecha a janela do administrador e exibe a janela de login novamente
        self.deiconify()

zoologico = App()
zoologico.mainloop()
