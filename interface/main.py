import sys
import tkinter

sys.path.append('./db_zoo/')

import database
import customtkinter as ctk
from PIL import Image, ImageTk, ImageFilter

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
        #configurações da janela do administrador
        janela_admin = subnivel(self)
        janela_admin.rowconfigure((0,1), weight=1)
        janela_admin.columnconfigure((0,1,2,3), weight=1)

        # Componentes da tela de administrador

        #configuração da barra menu no topo
        barra_menu = ctk.CTkFrame(master=janela_admin, height=150, corner_radius=0, fg_color='#9FB79F')
        barra_menu.grid(row=0, columnspan=4, column=0, sticky='ew')
        barra_menu.columnconfigure((0,1,2,3), weight=1)
        barra_menu.rowconfigure(0, weight=1, minsize=150)
    
        #botao funcionario
        icone_funcionario = ctk.CTkImage(light_image=Image.open('./imagens/icone_funcionario.png'), size=(80, 80))
        botao_funcionario = ctk.CTkButton(barra_menu, image=icone_funcionario, text='Funcionário', compound='left', height=150, border_spacing=5, corner_radius=0, fg_color='transparent',hover_color='#076E48', font=('Poppins',20,'bold'))
        botao_funcionario.grid(row=0, column=0, sticky='ew')

        #botão ambiente
        icone_ambiente = ctk.CTkImage(light_image=Image.open('./imagens/teste.png'), size=(80, 80))
        botao_ambiente = ctk.CTkButton(barra_menu, image=icone_ambiente, text='Ambiente', compound='left', height=150, border_spacing=5, corner_radius=0, fg_color='transparent',hover_color='#076E48', font=('Poppins',20,'bold'))
        botao_ambiente.grid(row=0, column=1, sticky='ew')

        #botão do estoque
        icone_estoque = ctk.CTkImage(light_image=Image.open('./imagens/teste.png'), size=(80, 80))
        botao_estoque = ctk.CTkButton(barra_menu, image=icone_estoque, text='Estoque', compound='left', height=150, border_spacing=5, corner_radius=0, fg_color='transparent',hover_color='#076E48', font=('Poppins',20,'bold'))
        botao_estoque.grid(row=0, column=2, sticky='ew')

        #botão sair
        icone_sair = ctk.CTkImage(light_image=Image.open('./imagens/teste.png'), size=(80, 80))
        botao_sair = ctk.CTkButton(barra_menu, image=icone_sair, text='Sair', compound='left', height=150, border_spacing=5, corner_radius=0, fg_color='transparent',hover_color='#076E48', font=('Poppins',20,'bold'))
        botao_sair.grid(row=0, column=3, sticky='ew')
        
        #frame do meio da tela
        barra_tela_principal = ctk.CTkFrame(master=janela_admin, height=900, corner_radius=0, fg_color='#fff')
        barra_tela_principal.grid(row=1, column=0, columnspan=4, sticky='ew')
        barra_tela_principal.columnconfigure((0,1,2,3), weight=1)
        barra_tela_principal.rowconfigure(0, weight=1, minsize=900)

        #foto
        foto = tkinter.Canvas(barra_tela_principal, width=200, height=200, bg="black", highlightthickness=0)

        imagem = Image.open('./imagens/eu.png')
        imagem_redimensionada = imagem.resize((150, 150), Image.LANCZOS)
        img = ImageTk.PhotoImage(imagem_redimensionada)
        foto.image = img  # Mantenha uma referência à imagem
        foto.create_oval(0, 0, 150, 150, fill="white", outline="green", width=6)
        foto.create_image(0,0, anchor=tkinter.NW, image=img)
     
        foto.grid(row=0, column=0)

        ''' #foto do administrador
        foto_administrador = ctk.CTkImage(Image.open('./imagens/eu.png'),size=(200,200))
        foto = ctk.CTkLabel(barra_tela_principal, image=foto_administrador, text="", fg_color='transparent')
        foto.grid(row=0, column=0, columnspan=2)
        '''
        
        
        
        '''

       

        
        
        

        esquerda_barra_menu = ctk.CTkFrame(master=barra_tela_principal,corner_radius=0, height=900, border_width=10)
        esquerda_barra_menu.grid(row=0,column=0, pady=5,padx=5)

        meio_barra_menu = ctk.CTkFrame(master=barra_tela_principal, corner_radius=0, height=900, border_width=5)
        meio_barra_menu.grid(row=0, column=1)
       
        direita_barra_menu = ctk.CTkFrame(master=barra_tela_principal, corner_radius=0, height=900, border_width=5)
        direita_barra_menu.grid(row=0, column=2)

        #componentes da janela administrador
        
    '''

        


    def logando(self):
        login = self.login.get()
        senha = self.senha.get()
        if login and senha:
            # Verifica as credenciais no banco de dados
            database.cursor.execute("SELECT * FROM users WHERE (Cpf=? and Senha=?)", (login, senha))
            result = database.cursor.fetchone()
            if result:
                tkinter.messagebox.showinfo('Login', 'Bem vindo!')
                self.withdraw()
                self.janela_administrador()  # Abre a janela de administrador
            else:
                tkinter.messagebox.showinfo('Falha', 'Credenciais inválidas')


zoologico = App()
zoologico.mainloop()


