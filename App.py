from tkinter import *
from Usuarios import Usuarios

class Application:
    def __init__(self, master=None):
        self.font = ("Verdana", "8")
        self.container1 = Frame(master, pady=10)
        self.container1.pack()
        self.container2 = Frame(master, padx=20, pady=5)
        self.container2.pack()
        self.container3 = Frame(master, padx=20, pady=5)
        self.container3.pack()
        self.container4 = Frame(master, padx=20, pady=5)
        self.container4.pack()
        self.container5 = Frame(master, padx=20, pady=5)
        self.container5.pack()
        self.container6 = Frame(master, padx=20, pady=5)
        self.container6.pack()
        self.container7 = Frame(master, padx=20, pady=5)
        self.container7.pack()
        self.container8 = Frame(master, padx=20, pady=10)
        self.container8.pack()
        self.container9 = Frame(master, pady=15)
        self.container9.pack()
        
        # Container 1
        self.titulo = Label(self.container1, text="Informe os dados: ", font=("Calibri", "9", "bold"))
        self.titulo.pack()
        
        # Container 2
        self.lbl_idusuario = Label(self.container2, text="idUsuário: ", font=self.font, width=10)
        self.lbl_idusuario.pack(side=LEFT)
        self.txt_idusuario = Entry(self.container2, width=10, font=self.font)
        self.txt_idusuario.pack(side=LEFT)
        self.btn_buscar = Button(self.container2, text="Buscar", font=self.font, width=10, command=self.buscar_Usuario)
        self.btn_buscar.pack(side=RIGHT)
        
        # Container 3
        self.lbl_nome = Label(self.container3, text="Nome", font=self.font, width=10)
        self.lbl_nome.pack(side=LEFT)
        self.txt_nome = Entry(self.container3, width=25, font=self.font)
        self.txt_nome.pack(side=LEFT)
        
        # Conteiner 4 telefone
        self.lbl_telefone = Label(self.container4, text="Telefone: ", font=self.font, width=10)
        self.lbl_telefone.pack(side=LEFT)
        self.txt_telefone = Entry(self.container4, width=25, font=self.font)
        self.txt_telefone.pack(side=LEFT)
        
        # Conteiner 5 email
        self.lbl_email = Label(self.container5, text="Email: ", font=self.font, width=10)
        self.lbl_email.pack(side=LEFT)
        self.txt_email = Entry(self.container5, width=25, font=self.font)
        self.txt_email.pack(side=LEFT)
        
        # Conteiner 6 usuario
        self.lbl_usuario = Label(self.container6, text="Usuario: ", font=self.font, width=10)
        self.lbl_usuario.pack(side=LEFT)
        self.txt_usuario = Entry(self.container6, width=25, font=self.font)
        self.txt_usuario.pack(side=LEFT)
        
        # Conteiner 7 senha
        self.lbl_senha = Label(self.container7, text="Senha", font=self.font, width=10)
        self.lbl_senha.pack(side=LEFT)
        self.txt_senha = Entry(self.container7, width=25, font=self.font, show="*")
        self.txt_senha.pack(side=LEFT)
        
        # Conteiner 8 iserir alterar excluir
        self.btn_Inserir = Button(self.container8, text="Inserir", font=self.font, width=12, command=self.Inserir_Usuario)
        self.btn_Inserir.pack(side=LEFT)
        self.btn_Alterar = Button(self.container8, text="Alterar", font=self.font, width=12, command=self.Alterar_Usuario)
        self.btn_Alterar.pack(side=LEFT)
        self.btn_Excluir = Button(self.container8, text="Excluir", font=self.font, width=12, command=self.Excluir_Usuario)
        self.btn_Excluir.pack(side=LEFT)

        # Conteiner 9 mensagem
        self.lbl_mensagem = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lbl_mensagem.pack()
        
    def Reset_Entry(self):
        # deixa as caixas em branco depois de executar
        self.txt_idusuario.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_usuario.delete(0, END)
        self.txt_senha.delete(0, END)
    
    def Inserir_Usuario(self):
        user = Usuarios()
        
        user.idusuario = self.txt_idusuario.get()
        user.nome = self.txt_nome.get()
        user.telefone = self.txt_telefone.get()
        user.email = self.txt_email.get()
        user.usuario = self.txt_usuario.get()
        user.senha = self.txt_senha.get()

        self.lbl_mensagem["text"] = user.insertUser()
        
        self.Reset_Entry()
        
    def Alterar_Usuario(self):
        user = Usuarios()
        
        user.idusuario = self.txt_idusuario.get()
        user.nome = self.txt_nome.get()
        user.telefone = self.txt_telefone.get()
        user.email = self.txt_email.get()
        user.usuario = self.txt_usuario.get()
        user.senha = self.txt_senha.get()

        self.lbl_mensagem["text"] = user.updateUser()
        
        self.Reset_Entry()
    
    def Excluir_Usuario(self):
        user = Usuarios()
        
        user.idusuario = self.txt_idusuario.get()

        self.lbl_mensagem["text"] = user.deleteUser()
        
        self.Reset_Entry()
        
    def buscar_Usuario(self):
        user = Usuarios()
        
        idusuario = self.txt_idusuario.get()
        
        self.lbl_mensagem["text"] = user.selectUser(idusuario)
        
        self.txt_idusuario.delete(0, END)
        self.txt_idusuario.insert(INSERT, user.idusuario)
        self.txt_nome.delete(0, END)
        self.txt_nome.insert(INSERT, user.nome)
        self.txt_telefone.delete(0, END)
        self.txt_telefone.insert(INSERT, user.telefone)
        self.txt_email.delete(0, END)
        self.txt_email.insert(INSERT, user.email)
        self.txt_usuario.delete(0, END)
        self.txt_usuario.insert(INSERT, user.usuario)
        self.txt_senha.delete(0, END)
        self.txt_senha.insert(INSERT, user.senha)
        
root = Tk()
Application(root)
root.mainloop()