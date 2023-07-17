import socket
import threading

clientes = []
temp = ''

print("Aguardando conexão de um cliente")


def novo_cliente():
    while True:
            cliente, porta = server.accept()
            clientes.append(cliente)
            print("Conectado em :", porta)
            threading.Thread(target=troca_mensagem, args=(cliente, porta)).start()

def troca_mensagem(cliente, porta):
    while True:
        mensagem_decodificada = cliente.recv(2048).decode()
        
        if mensagem_decodificada.split(',')[0].upper() == 'ADICAO':  
            cliente.send(servidor_adicao(mensagem_decodificada).encode())
        elif mensagem_decodificada.split(',')[0].upper() == 'SUBTRACAO':
            cliente.send(servidor_subtracao(mensagem_decodificada).encode())
        else:   print('Entrada não reconhecida.')
        

def servidor_adicao(msg):
    HOST = 'localhost'
    PORTA = 60000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))
    client.send(msg.encode())
    return client.recv(2048).decode()


def servidor_subtracao(msg):
    HOST = 'localhost'
    PORTA = 60001
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))
    client.send(msg.encode())
    return client.recv(2048).decode()


if __name__ == '__main__':
    HOST = 'localhost'
    PORTA = 50000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORTA))
    server.listen(5)
    threading.Thread(target=novo_cliente(), args=()).start()
