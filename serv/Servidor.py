from socket import *
from threading import Thread

# Matheus Felipe Vieira Santiago
# servidor de chat socket 

def recebendo_msg(conn, addr):
    global conns 
    while True:
        try:
            #tenta receber mensagens od cliente 
            msg = conn.recv(1024)
            if not msg:
                break
            print(f"{msg.decode()}")
            enviar_msg(msg)
        except:
            conn.close() #fecha a conexao

            conns.remove(conn) #remove da lsita
            print(f"{addr} saiu")
            break


def enviar_msg(data):
    global conns
    for c in conns:#envia a msg para todos no chat
        c.send(data)
        print("Enviada")
conns = [] #lista de conexoes
#meu socket
s = socket(AF_INET, SOCK_STREAM) #socket
s.bind((gethostname(),55551)) #caminhos
s.listen(5) #maximo de usuarios
print(f"IP SERVIDOR: {gethostname()} Porta: {55551}") #print ilustrativa

while True:
    #essa parte do codigo fica criando conexões
    conn, addr = s.accept()
    t = Thread(target=recebendo_msg, args=(conn,addr))
    t.start()
    conns.append(conn)
    print(conns[-1])



