# Interface e Escrita por PKAPA {Emerson}
# Socket escrito e codificado por Meguinha {Meguinha}
# Chat v0.1
from Gui.gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
from threading import *
import sys




cSocket = socket(AF_INET, SOCK_STREAM)
conexao = False

class Chat(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Chat, self).__init__()
        self.setupUi(self)

        # ATRIBUI FUNÇÕES AOS BOTOES DA INTERFACE
        self.btnEnviar.clicked.connect(self.buttonEnviar)
        self.btnConectar.clicked.connect(self.conectar)
        self.btnAlterar.clicked.connect(self.apelidoAlterar)
        self.entryEnviar.returnPressed.connect(self.btnEnviar.click)


    # --------- MÉTODOS --------------
    def buttonEnviar(self):
        if conexao:
            msg = f'{self.apelido}: {self.entryEnviar.text()}'
            self.enviar(msg)
            self.entryEnviar.clear()
        else:
            self.txtChat.append('SEM CONEXÃO !')


    def conectar(self):
        self.ip = self.entryIp.text()
        self.porta = self.entryPort.text()
        self.apelido = gethostname()

        global conexao
        try:
            cSocket.connect((self.ip, 55551))
            print(f'Conectado ao servidor: {self.ip} com Sucesso !')
            cSocket.send(bytes(f'{gethostname()} conectou ao servidor', 'utf-8'))
            self.thread()
            conexao = True
        except:
            print(f'ERROR: Não foi possível conectar ao servidor: {self.ip}')
            self.txtChat.append(f'Não foi possível conectar ao servidor: {self.ip}')
            #messagebox.showerror('ERROR', f'Não foi possível conectar ao servidor: {self.ip}')

    
    def apelidoAlterar(self):
        if conexao:
            self.enviar(f'{self.apelido} mudou seu apelido para {self.entryApelido.text()}')
            self.apelido = self.entryApelido.text()
        else:
            print('Sem Conexão')
            self.txtChat.append('SEM CONEXÃO !')


    # -----------------------------------------------------------------------------------
    # ----------- THREAD ------------
    def thread(self):
        t = Thread(target=self.receber)
        t.start()

    # ------------- Socket --------------
    def enviar(self, msg):
        try:
            if conexao:
                cSocket.send(bytes(f'{msg}', 'utf-8'))
            else:
                print("Sem Conexão")
                self.txtChat.append('SEM CONEXÃO !')
                #messagebox.showerror('ERROR', f'Sem Conexão')
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
                    self.txtChat.append(f'{data.decode()}')
                    print(f'{data.decode()}\n')
            except:
                pass

        


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    ui = Chat()
    ui.show()
    sys.exit(app.exec_())
