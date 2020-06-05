''' 
@utf-8
13/03/2020
emersonv25
Meguinha

Alunos d

'''

from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from socket import *
from threading import *

cSocket = socket(AF_INET, SOCK_STREAM)

conexao = False


class Chat:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.titulo = 'Chatroom do emersonv25 e Meguinha v0.4'
        self.tamanho = '560x480'
        # Criando a janela
        self.master.title(self.titulo)
        self.master.geometry(self.tamanho)

        # ------------- WIDGtE ----------------------------------

        # Objetos da interface
        self.txtChat = scrolledtext.ScrolledText()
        self.buttonOK = Button(width=5, height=3, text="Enviar", command=self.buttonEnviar)
        self.buttonConnect = Button(width=10, height=5, text="Connect", command=self.ipConnect)
        self.buttonApelido = Button(width=5, height=1, text="Alterar", command=self.apelidoAlterar)
        self.entrada = Entry()
        self.apelidoEntry = Entry()
        self.apelidoLbl = Label(text="Apelido: ")
        self.master.bind('<Return>', self.buttonReturn)

        # menuzinho
        self.menu = Menu(self.master)
        self.menuOpc = Menu(self.menu)
        self.menuOpc.add_command(label="Conectar", command=self.ipConnect)
        #self.menuOpc.add_command(label="Sair", command=self.sair)
        self.menu.add_cascade(label="Opções", menu=self.menuOpc)
        self.master.config(menu=self.menu)

        # Tamanho e Posicionamento
        self.apelidoLbl.place(x=430, y=25)
        self.buttonApelido.place(x=470, y=80)
        self.apelidoEntry.place(x=430, y=50)
        self.txtChat.place(x=30, y=25, width=400, height=300)
        self.buttonOK.place(x=430, y=400)
        self.buttonConnect.place(x=450, y=125)
        self.entrada.place(x=20, y=400, width=400, height=50)

        # -----------------Inicializa a janela ---------------
        self.frame.pack()

        # ------------------- SOCKET -----------------------------

        self.apelido = gethostname()

    # ------------------- MÉTODOS ------------------------
    def sair(self):
        if messagebox.askyesno("Fechar Janela", "Tem certeza que deseja Sair ?"):
            if conexao:
                print("Desconectou")
                self.enviar(f'{self.apelido} Desconectou do servidor.')
                exit()
            exit()

    def apelidoAlterar(self):
        if conexao:
            self.enviar(f'{self.apelido} mudou seu apelido para {self.apelidoEntry.get()}')
            self.apelido = self.apelidoEntry.get()
        else:
            messagebox.showerror('ERROR', f'Sem Conexão')

    def thread(self):
        t = Thread(target=self.receber)
        t.start()

    def ipConnect(self):
        self.newWindow = Toplevel(self.master)
        self.tela = Ip(self.newWindow)
        self.tela.carregar()

    def buttonEnviar(self):
        msg = f'{self.apelido}: {self.entrada.get()}'
        self.enviar(msg)
        self.entrada.delete(0, 'end')

    def buttonReturn(self, event=None):
        msg = f'{self.apelido}: {self.entrada.get()}'
        self.enviar(msg)
        self.entrada.delete(0, 'end')

    def enviar(self, msg):
        try:
            if conexao:
                cSocket.send(bytes(f'{msg}', 'utf-8'))
            else:
                messagebox.showerror('ERROR', f'Sem Conexão')
        except:
            pass

    def receber(self):
        while True:
            try:
                data = cSocket.recv(1024)
                print(data)
                if not data:
                    break
                else:
                    self.txtChat.insert(INSERT, f'{data.decode()}\n')
                    print(f'{data.decode()}\n')
            except:
                pass


class Ip:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.titulo = 'connect'
        self.tamanho = '250x80'

        # Criando os objetos da interface

        self.label1 = Label(self.frame, text="IP: ")
        self.label2 = Label(self.frame, text="Port: ")
        # self.label3       = Label  (self.frame, text= "Apelido: ")
        self.EntryIP = Entry(self.frame, width=20)
        self.EntryPort = Entry(self.frame, width=20)
        # self.EntryApelido = Entry  (self.frame)
        self.ButtonIP = Button(self.frame, height=3, width=5, text="Entrar", command=self.entrar)

        # Posicionando
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.EntryIP.grid(row=0, column=1, columnspan=2)
        self.EntryPort.grid(row=1, column=1, columnspan=2)
        # self.EntryApelido.grid (row=3, column=1)
        # self.label3.grid  (row=3, column=0)
        self.ButtonIP.grid(row=0, column=3, columnspan=3, rowspan=2)

        # variaveis
        # Inicialização
        # self.connected = bool

    def carregar(self):
        self.master.title(self.titulo)
        self.master.geometry(self.tamanho)

        self.frame.grid()

    def entrar(self):
        self.ip = self.EntryIP.get()  # self.EntryIP.get()
        # self.apelido = self.EntryApelido.get() #self.EntryApelido.get()
        global conexao
        try:
            cSocket.connect((self.ip, 55551))
            print(f'Conectado ao servidor: {self.ip} com Sucesso !')
            cSocket.send(bytes(f'{gethostname()} conectou ao servidor', 'utf-8'))
            tela.thread()
            conexao = True
            self.master.destroy()
        except:
            print(f'ERROR: Não foi possível conectar ao servidor: {self.ip}')
            messagebox.showerror('ERROR', f'Não foi possível conectar ao servidor: {self.ip}')

            # def getIp(self):
    #    return self.ip
    # def getApelido(self):
    #    return self.apelido  


root = Tk()
tela = Chat(root)
root.mainloop()
